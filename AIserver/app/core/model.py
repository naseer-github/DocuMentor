from pathlib import Path

import chromadb
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from sentence_transformers import SentenceTransformer

from app.core.paths import AI_SERVER_ROOT
from .config import GEMINI_API_KEY

if not GEMINI_API_KEY:
    raise RuntimeError(
        "AI server: missing Gemini API key. Create a file AIserver/.env with a line "
        "GEMINI_API=your_key (see AIserver/.env.example). Keys: https://aistudio.google.com/apikey"
    )

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GEMINI_API_KEY,
)

embedding_model = SentenceTransformer(
    "nomic-ai/nomic-embed-text-v1", trust_remote_code=True)

CHROMA_DIR = str(AI_SERVER_ROOT / "chroma_dbs")
Path(CHROMA_DIR).mkdir(parents=True, exist_ok=True)
chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
