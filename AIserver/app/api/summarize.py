from fastapi import APIRouter, Form, HTTPException
from app.services.summarizer import summarize_text

router = APIRouter()


@router.post("/summarize/")
async def summarize(
    passage: str = Form(...),
    document_type: str = Form("general"),
    summary_length: int = Form(20),
    format_preference: str = Form("outline"),
    focus: str = Form("main ideas")
):
    print("🌐 DEBUG: /summarize/ endpoint called")
    print(f"🌐 DEBUG: Received parameters:")
    print(f"   - passage length: {len(passage)}")
    print(f"   - document_type: {document_type}")
    print(f"   - summary_length: {summary_length}")
    print(f"   - format_preference: {format_preference}")
    print(f"   - focus: {focus}")

    result = summarize_text(passage, document_type, summary_length, format_preference, focus)

    print(f"🌐 DEBUG: Got result from summarize_text: {type(result)}")
    if isinstance(result, dict):
        print(f"🌐 DEBUG: Result keys: {result.keys()}")

    if isinstance(result, dict) and result.get("error"):
        print(f"🌐 DEBUG: Error detected, raising HTTPException: {result['error']}")
        raise HTTPException(status_code=503, detail=result["error"])

    print("🌐 DEBUG: Returning successful result")
    return result
