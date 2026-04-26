import re
from app.core.model import llm, get_embedding_model, chroma_client
from app.prompts.search import (
    get_similar_questions_prompt,
    get_answer_prompt,
    get_extraction_prompt
)


# ----------------------------
# Generate query variations
# ----------------------------
def generate_similar_questions(query: str):
    prompt = get_similar_questions_prompt(query)
    response = llm.invoke(prompt)

    raw_lines = response.content.strip().split('\n')

    questions = [query]

    for line in raw_lines:
        line = line.strip()

        if not line or len(questions) >= 6:
            continue

        # remove numbering like "1." or "1)"
        line = re.sub(r'^\d+[\.)]\s*', '', line)

        if line:
            questions.append(line)

    return questions


# ----------------------------
# Chroma filter builder
# ----------------------------
def applyFilters(start_page, end_page):
    if start_page is not None and end_page is not None:
        return {
            "$and": [
                {"page_number": {"$gte": start_page}},
                {"page_number": {"$lte": end_page}}
            ]
        }

    if start_page is not None:
        return {"page_number": {"$gte": start_page}}

    if end_page is not None:
        return {"page_number": {"$lte": end_page}}

    return None


# ----------------------------
# Main RAG search function
# ----------------------------
def search_document(
    document_id: str,
    query: str,
    top_k: int = 5,
    start_page=None,
    end_page=None
):
    collection = chroma_client.get_or_create_collection(f"doc_{document_id}")

    embedding_model = get_embedding_model()

    similar_questions = generate_similar_questions(query)

    all_results = []

    for question in similar_questions:
        try:
            embedding = embedding_model.encode(
                ["search_query: " + question],
                normalize_embeddings=True
            )[0].tolist()

            where_filter = applyFilters(start_page, end_page)

            results = collection.query(
                query_embeddings=[embedding],
                n_results=top_k,
                where=where_filter
            )

            if not results or not results.get("ids"):
                continue

            for i in range(len(results["ids"][0])):
                metadata = results["metadatas"][0][i] or {}

                all_results.append({
                    "id": results["ids"][0][i],
                    "text": metadata.get("text", ""),
                    "distance": results["distances"][0][i],
                    "question": question
                })

        except Exception as e:
            print(f"Search error for question '{question}': {e}")
            continue

    # ----------------------------
    # Remove duplicates safely
    # ----------------------------
    seen = set()
    unique = []

    for r in all_results:
        text = r.get("text", "").strip()
        if text and text not in seen:
            seen.add(text)
            unique.append(r)

    context = "\n\n".join(r["text"] for r in unique)

    # ----------------------------
    # Generate final answer
    # ----------------------------
    answer_prompt = get_answer_prompt(query, context)
    answer = llm.invoke(answer_prompt).content

    # ----------------------------
    # Extract exact source
    # ----------------------------
    extraction_prompt = get_extraction_prompt(query, context, answer)
    exact_source = llm.invoke(extraction_prompt).content

    return {
        "answer": answer,
        "exact_source": exact_source,
    }