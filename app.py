import gradio as gr
import openai

# Set your OpenAI API key here
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

# Define the input components
question_input = gr.Textbox(label="Question")
answer_input = gr.Textbox(label="Answer")
marks_input = gr.Number(label="Marks")

# Define the output component
response_output = gr.Textbox(label="Response")

# Define a function to generate the model's response when the "Submit" button is clicked
def generate_response(question, answer, marks, submit_button):
    if submit_button:
        messages = [
            {"role": "system", "content": """ model is acting as a UPSC Paper Checker.
    It should evaluate answers based on:
    Contextual relevance
    Grammar
    Related information
    It should provide marks out of a maximum score.
    Suggestions for improvement should be given.
    Feedback should be structured in a pointwise manner.
    Specific grading criteria for answers:
             I Want the Marks in Bold section
    4-5 marks for a normal representation of the answer.
    6-7 marks for well-mannered answers with good information and more than 150 words.
    8-9 marks for answers that excel in all parameters, but the word count must be greater than 200.
    10 marks are not to be given unless all criteria are met."""},
            {"role": "user", "content": f"Que){question} Ans){answer} Marks){marks}"}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=250
        )

        return response.choices[0].message["content"]

# Create the Gradio interface without live rendering
iface = gr.Interface(
    fn=generate_response,
    inputs=[question_input, answer_input, marks_input, gr.Button("Submit")],
    outputs=response_output,
    theme="default"
)

# Launch the interface on a local server
iface.launch(share=True)
