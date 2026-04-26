
# prompts/quiz.py
def get_quiz_prompt_from_chunk(text: str, answer_formats: list[str], question_type: str = "mixed") -> str:
    format_instructions = []
    examples = []

    if "mcq" in answer_formats:
        format_instructions.append(
            "- multiple-choice questions (MCQs) with options A-D")
        examples.append("""
- MCQ:
QUESTION: ...
OPTIONS:
A. ...
B. ...
C. ...
D. ...
ANSWER: B
END""")

    if "true/false" in answer_formats:
        format_instructions.append("- True/False questions")
        examples.append("""
- True/False:
QUESTION: ...
ANSWER: True
END""")

    if "short" in answer_formats:
        format_instructions.append(
            "- short answer questions without options(1-2 lines answers)")
        examples.append("""
- Short:
QUESTION: ...
ANSWER: ...(1-2 lines answers)
END""")

    if "long" in answer_formats:
        format_instructions.append(
            "- long-form descriptive questions(descriptive answers)")
        examples.append("""
- Long:
QUESTION: ...
ANSWER: ... (Long descriptive answer expected)
END""")

    type_instruction = ""
    if question_type == "factual":
        type_instruction = "Focus only on fact-based questions like definitions, lists, or direct information from the text."
    elif question_type == "conceptual":
        type_instruction = "Generate questions that test understanding, reasoning, and interpretation based on the content."
    elif question_type == "mixed":
        type_instruction = "Include a mix of both factual and conceptual questions."

    # Pre-build the bullet list to avoid backslashes inside an f-string expression.
    formatted_instructions = "\n- ".join(format_instructions)

    return f"""
Based on the following text, generate only relevant questions of the following types:
- {formatted_instructions}

If the text does not contain enough information for a relevant question type, do not generate that question.
If no questions are relevant at all, respond with: NO QUESTIONS

{text}

Instructions:
{type_instruction}

Format examples:
{''.join(examples)}
"""


def get_mark_quiz_prompt(questions: list, answers: list) -> str:
    """
    Generate a prompt to mark multiple quiz answers at once.
    """
    quiz_items = []
    for i, (q, a) in enumerate(zip(questions, answers)):
        quiz_items.append(f"""
Question {i+1}:
Type: {q.get('type', 'unknown')}
Question: {q['question']}
Correct Answer: {q['correct_answer']}
User Answer: {a}
""")

    return f"""
You are an automated quiz grading assistant. Grade the following quiz answers.

For each question:
- Provide a score (0-5 for long questions, 0-2 for short questions)
- Give brief feedback explaining the score
- Format: "Question X: Score Y/5 - Feedback: [explanation]"

Quiz to grade:
{''.join(quiz_items)}

Output only the scores and feedback, one per line.
"""
