import gradio as gr

def greet():
    return "Hello World from Codespaces!"

demo = gr.Interface(
    fn=greet,
    inputs=None,
    outputs="text"
)

demo.launch()
