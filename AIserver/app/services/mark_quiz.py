

from app.core.model import llm
from app.prompts.quiz import get_mark_quiz_prompt


def mark_quiz(questions: list, answers: list) -> dict:
    """
    Marks quiz answers using Gemini AI.

    Args:
        questions: List of question dicts with 'question' and 'correct_answer'
        answers: List of user answer strings

    Returns:
        Dict with scores and feedback
    """
    if len(questions) != len(answers):
        return {"error": "Questions and answers count mismatch"}

    prompt = get_mark_quiz_prompt(questions, answers)

    try:
        response = llm.invoke(prompt)
        # Parse the response to extract scores and feedback
        # This would need to be implemented based on the prompt format
        return {
            "total_questions": len(questions),
            "marked_answers": response.content,
            "model_used": "gemini-2.0-flash"
        }
    except Exception as e:
        return {"error": str(e)}