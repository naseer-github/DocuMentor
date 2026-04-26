from fastapi import Form, APIRouter, HTTPException
from app.prompts.explanation import get_explanation_prompt
from app.core.model import generate_content


router = APIRouter()


@router.post("/explanation/")
async def explain_text(
    passage: str = Form(...),
    detail_level: str = Form("medium")  # can be: simple, medium, in-depth
):
    prompt = get_explanation_prompt(passage, detail_level)
    print(prompt)
    try:
        response_text = generate_content(prompt)
        return {
            "explanation": response_text.strip(),
            "detail_level": detail_level
        }
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
