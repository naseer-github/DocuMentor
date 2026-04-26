from app.core.model import generate_content
from app.prompts.summarization import (
    get_summary_continue_prompt,
    get_summary_intro_prompt,
    get_summarize_text_prompt
)


# ----------------------------
# SINGLE PASS SUMMARIZATION
# ----------------------------
def summarize_text(
    passage: str,
    document_type: str,
    summary_length: str,
    format_preference: str,
    focus: str
):
    print(f"🔍 DEBUG: summarize_text called with:")
    print(f"   - passage length: {len(passage)}")
    print(f"   - document_type: {document_type}")
    print(f"   - summary_length: {summary_length}")
    print(f"   - format_preference: {format_preference}")
    print(f"   - focus: {focus}")

    prompt = get_summarize_text_prompt(
        passage,
        document_type,
        summary_length,
        format_preference,
        focus
    )

    print(f"🔍 DEBUG: Generated prompt length: {len(prompt)}")
    print(f"🔍 DEBUG: Prompt preview: {prompt[:200]}...")

    try:
        print("🔍 DEBUG: Calling generate_content...")
        response = generate_content(prompt)
        print(f"🔍 DEBUG: Got response, length: {len(response)}")
        print(f"🔍 DEBUG: Response preview: {response[:200]}...")

        return {
            "summary": response,
            "model_used": "gemini-2.0-flash"
        }

    except Exception as e:
        print(f"❌ DEBUG: Exception in summarize_text: {e}")
        return {"error": str(e)}


# ----------------------------
# CHUNK-BASED PDF SUMMARIZATION
# ----------------------------
def summarize_pdf(
    chunks: list,
    document_type: str = "general",
    summary_length: int = 40,
    format_preference: str = "paragraph",
    focus: str = "main ideas"
) -> str:

    context = ""
    summaries = []

    for i, chunk in enumerate(chunks):

        if context:
            prompt = get_summary_continue_prompt(
                context,
                chunk,
                document_type=document_type,
                summary_length=summary_length,
                format_preference=format_preference,
                focus=focus
            )
        else:
            prompt = get_summary_intro_prompt(
                chunk,
                document_type=document_type,
                summary_length=summary_length,
                format_preference=format_preference,
                focus=focus
            )

        try:
            response = generate_content(prompt)
            summary = response.strip()

            if summary:
                summaries.append(summary)
                context += "\n" + summary

        except Exception as e:
            print(f"Error summarizing chunk {i}: {e}")
            continue

    return "\n\n".join(summaries)