import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from app.core.paths import AI_SERVER_ROOT, REPO_ROOT

# Load env from AIserver first, then repo root (without overriding already-set vars).
load_dotenv(AI_SERVER_ROOT / ".env")
load_dotenv(REPO_ROOT / ".env", override=False)

GEMINI_API_KEY = (
    os.getenv("GEMINI_API")
    or os.getenv("GEMINI_API_KEY")
    or os.getenv("GOOGLE_API_KEY")
)


def add_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
