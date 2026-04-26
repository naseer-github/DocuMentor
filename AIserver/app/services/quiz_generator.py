from app.core.model import generate_content
from app.prompts.quiz import get_quiz_prompt_from_chunk
import re


def generate_quiz_from_chunks(
    chunks: list,
    answer_formats: list[str],
    question_type: str = "mixed"
) -> list:

    quiz = []

    for chunk in chunks:
        prompt = get_quiz_prompt_from_chunk(
            chunk, answer_formats, question_type
        )

        try:
            response = generate_content(prompt).strip()

            # ----------------------------
            # Skip invalid AI response
            # ----------------------------
            if not response or response.upper() == "NO QUESTIONS":
                continue

            # ----------------------------
            # Split questions
            # ----------------------------
            question_blocks = response.split("END")

            for block in question_blocks:
                block = block.strip()
                if not block:
                    continue

                q_data = {}
                lines = block.splitlines()

                current_type = None
                options_started = False
                collecting_answer = False
                answer_lines = []

                for i, line in enumerate(lines):
                    line = line.strip()

                    # ----------------------------
                    # Question type
                    # ----------------------------
                    if i == 0:
                        match = re.match(
                            r"^- (MCQ|Short|Long|True/False):",
                            line,
                            re.IGNORECASE
                        )
                        if match:
                            current_type = match.group(1).strip().lower()
                            q_data["type"] = current_type

                    # ----------------------------
                    # Question text
                    # ----------------------------
                    elif line.startswith("QUESTION:"):
                        q_data["question"] = line.replace("QUESTION:", "").strip()

                    # ----------------------------
                    # Options
                    # ----------------------------
                    elif line.startswith("OPTIONS:"):
                        q_data["options"] = []
                        options_started = True

                    elif options_started and re.match(r"^[A-D]\.", line):
                        q_data["options"].append(line[2:].strip())

                    # ----------------------------
                    # Answer
                    # ----------------------------
                    elif line.startswith("ANSWER:"):
                        answer_text = line.replace("ANSWER:", "").strip()
                        collecting_answer = True

                        # MCQ single-letter answer
                        if "options" in q_data and answer_text.upper() in "ABCD":
                            idx = "ABCD".index(answer_text.upper())
                            q_data["answer"] = (
                                q_data["options"][idx]
                                if idx < len(q_data["options"])
                                else answer_text
                            )
                            collecting_answer = False
                        else:
                            answer_lines = [answer_text] if answer_text else []

                    # ----------------------------
                    # Multi-line answer support
                    # ----------------------------
                    elif collecting_answer:
                        answer_lines.append(line)

                # finalize long answers
                if collecting_answer and answer_lines:
                    q_data["answer"] = " ".join(answer_lines).strip()

                # ----------------------------
                # Validate before adding
                # ----------------------------
                if (
                    "question" in q_data and
                    "answer" in q_data and
                    "type" in q_data
                ):
                    quiz.append(q_data)

        except Exception as e:
            print(f"Error generating quiz: {e}")
            continue

    return quiz