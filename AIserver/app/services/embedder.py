from app.core.model import get_embedding_model, chroma_client
from app.core.paths import resolve_server_file
from langchain_community.document_loaders import PyPDFLoader


def chunk_text(text, page_num, chunk_size=300):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = "search_document: " + " ".join(words[i:i + chunk_size])
        chunks.append((chunk, page_num))

    return chunks


def embed_pdf(file_path: str, doc_id: str):
    try:
        loader = PyPDFLoader(resolve_server_file(file_path))
        pages = loader.load()

        all_chunks, page_nums = [], []

        for page in pages:
            text = page.page_content
            if not text.strip():
                continue  # ✅ skip empty pages

            page_num = page.metadata["page"] + 1
            chunks = chunk_text(text, page_num)

            for chunk, page_no in chunks:
                all_chunks.append(chunk)
                page_nums.append(page_no)

        if not all_chunks:
            return {"error": "No valid text found in document"}

        # ✅ Generate embeddings
        embeddings = get_embedding_model().encode(
            all_chunks, convert_to_numpy=True
        ).tolist()

        collection_name = f"doc_{doc_id}"
        collection = chroma_client.get_or_create_collection(collection_name)

        # ✅ Optional: prevent duplicates
        try:
            collection.delete(where={"doc_id": doc_id})
        except:
            pass

        collection.add(
            ids=[f"{doc_id}_{i}" for i in range(len(all_chunks))],
            embeddings=embeddings,
            metadatas=[
                {
                    "doc_id": doc_id,
                    "page_number": page_no,
                    "text": chunk
                }
                for chunk, page_no in zip(all_chunks, page_nums)
            ]
        )

        return {
            "message": "Document embedded successfully",
            "document_id": doc_id,
            "chunks": len(all_chunks)
        }

    except Exception as e:
        print("❌ Embedding Error:", str(e))
        return {"error": str(e)}