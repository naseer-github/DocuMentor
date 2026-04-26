import markdown
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.paths import resolve_server_file


# ----------------------------
# PDF TEXT EXTRACTION
# ----------------------------
def extract_text_from_pdf(file_path: str, start_page: int, end_page: int) -> str:
    loader = PyPDFLoader(resolve_server_file(file_path))
    pages = loader.load()

    # safer slicing (avoid index crash)
    selected_pages = pages[start_page - 1:end_page]

    return "\n\n".join(page.page_content for page in selected_pages)


# ----------------------------
# TEXT CHUNKING (RAG READY)
# ----------------------------
def chunk_document(text: str, chunk_size: int = 7500) -> list:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=100
    )
    return splitter.split_text(text)


# ----------------------------
# MARKDOWN → PDF EXPORT
# ----------------------------
def convert_summary_to_pdf(summary_markdown: str, output_path: str):
    # Import here to avoid system dependency crash
    from weasyprint import HTML

    html = markdown.markdown(summary_markdown)

    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: 'Times New Roman', Times, serif;
                line-height: 1.6;
                padding: 20px;
            }}
            h1, h2, h3 {{
                color: #333;
            }}
            strong {{
                font-weight: bold;
            }}
            em {{
                font-style: italic;
            }}
            code {{
                background: #f4f4f4;
                padding: 2px 4px;
                border-radius: 4px;
            }}
        </style>
    </head>
    <body>
        {html}
    </body>
    </html>
    """

    HTML(string=styled_html).write_pdf(output_path)