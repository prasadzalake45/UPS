# gradio_ui.py

import openai

def generate_response(question, answer, marks):
    # Include user-provided marks in the user message
    user_message = f"Que){question} Ans){answer} Marks){marks}"

    messages = [
        {"role": "system", "content": """ model is acting as a UPSC Paper Checker.
It should evaluate answers based on:
Contextual relevance
Grammar
Related information
It should me more accurately and give a more prominent response
It should provide marks out of a maximum score.
Suggestions for improvement should be given.
Feedback should be structured in a pointwise manner.
Specific grading criteria for answers:
I Want the Marks in Bold section
4-5 marks for a normal representation of the answer.
6-7 marks for well-mannered answers with good information and more than 150 words.
8-9 marks for answers that excel in all parameters, but the word count must be greater than 200.
10 marks are not to be given unless all criteria are met."""},
        {"role": "user", "content": user_message}
    ]

    # Extract user-provided marks
    user_marks = int(marks)

    # Determine the grade based on the user-provided marks
    if user_marks >= 8 and len(answer.split()) > 200:
        grade = 10
    elif user_marks >= 6 and len(answer.split()) > 150:
        grade = 8
    elif user_marks >= 4:
        grade = 6
    else:
        grade = 4

    # Update the system message with the determined grade
    messages[0]["content"] = messages[0]["content"].replace("I Want the Marks in Bold section", f"I Want the Marks in Bold section\n**Marks: {grade}**")

    return messages
