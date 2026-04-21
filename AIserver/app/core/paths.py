"""Repo layout: <repo>/AIserver (this service) and <repo>/server (Node uploads)."""
from pathlib import Path

# app/core/paths.py -> parents[2] == AIserver root
AI_SERVER_ROOT = Path(__file__).resolve().parents[2]
REPO_ROOT = AI_SERVER_ROOT.parent


def resolve_server_file(relative_file_path: str) -> str:
    """Turn a path stored on Document.file (relative to server/) into an absolute path."""
    return str(REPO_ROOT / "server" / relative_file_path)
