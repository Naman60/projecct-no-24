from pywebio.input import input, textarea, radio, checkbox
from pywebio.output import put_text, put_html, put_markdown

def main():
    put_markdown("## Welcome to the 10 Question Quiz!")

    # Ask 10 questions
    answers = {}
    for i in range(1, 11):
        question = f"What is your answer to question {i}?"
        answers[f"question_{i}"] = input(question, type=textarea)

    # Display answers
    put_markdown("## Your Answers:")
    for question, answer in answers.items():
        put_html(f"<b>{question}:</b> {answer}")

if __name__ == "__main__":
    main()
