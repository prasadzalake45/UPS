# run.py

import gradio as gr
from gradio_ui import generate_response
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

# Define a function to connect the UI with the generation function
def generate_and_format_response(question, answer, marks, submit_button):
    if submit_button:
        messages = generate_response(question, answer, marks)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=messages,
            temperature=0.7,
            max_tokens=250
        )

        return response.choices[0].message["content"]

# Create the Gradio interface without live rendering
iface = gr.Interface(
    fn=generate_and_format_response,
    inputs=[question_input, answer_input, marks_input, gr.Button("Submit")],
    outputs=response_output,
    theme="default"
)

# Launch the interface on a local server
iface.launch(share=True)
