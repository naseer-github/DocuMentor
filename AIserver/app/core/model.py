from pathlib import Path
import os

import chromadb
from sentence_transformers import SentenceTransformer
import google.genai as genai

from app.core.paths import AI_SERVER_ROOT
from .config import GEMINI_API_KEY

# Configure Google Gemini API
client = genai.Client(api_key=GEMINI_API_KEY)

# -------------------------------
# ✅ GOOGLE GEMINI MODEL
# -------------------------------
def get_gemini_client():
    return client

# LangChain LLM wrapper for Gemini
class GeminiLLM:
    def invoke(self, prompt):
        class Response:
            def __init__(self, content):
                self.content = content
        return Response(generate_content(prompt))

llm = GeminiLLM()

# -------------------------------
# ✅ EMBEDDING MODEL (FIXED)
# -------------------------------
_embedding_model = None

def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        os.environ.setdefault('HF_HOME', str(AI_SERVER_ROOT / '.hf_cache'))

        _embedding_model = SentenceTransformer(
            "nomic-ai/nomic-embed-text-v1",
            trust_remote_code=True
        )
    return _embedding_model


# -------------------------------
# ✅ GOOGLE GEMINI TEXT GENERATION
# -------------------------------
def generate_content(prompt: str) -> str:
    print(f"🤖 DEBUG: generate_content called with prompt length: {len(prompt)}")
    print(f"🤖 DEBUG: Prompt preview: {prompt[:100]}...")

    try:
        api_client = get_gemini_client()
        print("🤖 DEBUG: Got API client, calling models.generate_content...")

        response = api_client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config={
                "max_output_tokens": 512,
                "temperature": 0.7,
                "top_p": 0.9,
            }
        )

        print(f"🤖 DEBUG: Got response from API, text length: {len(response.text)}")
        print(f"🤖 DEBUG: Response preview: {response.text[:100]}...")

        return response.text

    except Exception as e:
        print(f"❌ DEBUG: Exception in generate_content: {e}")
        raw_error = str(e)
        error_type = type(e).__name__
        error_message = f"Google Gemini API request failed: {error_type} - {raw_error}"
        print("❌", error_message)
        print(f"Exception details: {repr(e)}")
        raise RuntimeError(error_message)


# -------------------------------
# ✅ CHROMA DB SETUP
# -------------------------------
CHROMA_DIR = str(AI_SERVER_ROOT / "chroma_dbs")
Path(CHROMA_DIR).mkdir(parents=True, exist_ok=True)

chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)