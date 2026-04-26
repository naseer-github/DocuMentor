import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from app.core.paths import AI_SERVER_ROOT, REPO_ROOT

# Load env from AIserver first, then repo root (without overriding already-set vars).
load_dotenv(AI_SERVER_ROOT / ".env")
load_dotenv(REPO_ROOT / ".env", override=False)

GEMINI_API_KEY = (
    os.getenv("GEMINI_API_KEY")
    or os.getenv("GOOGLE_API_KEY")
)

if not GEMINI_API_KEY:
    raise RuntimeError(
        "AI server: missing Google Gemini API key. Create a file AIserver/.env with:\n"
        "GEMINI_API_KEY=your_key"
    )


def add_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
