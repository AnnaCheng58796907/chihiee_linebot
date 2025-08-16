import gradio as gr

with gr.Blocks() as demo:
    a = gr.Number(label='數字A', value=0)
    b = gr.Number(label='數字B', value=0)

    with gr.Row():
        add_button = gr.Button('加法')
        subract_button = gr.Button('減法')
        multiply_button = gr.Button('乘法')
        divide_button = gr.Button('除法')

    c = gr.Number(label='結果', value=0)

    @add_button.click(
        inputs=[a, b],
        outputs=[c]
    )
    def add(x, y):
        return x + y
    
    @subract_button.click(
        inputs=[a, b],
        outputs=[c]
    )
    def subtract(x, y):
        return x - y
    
    @multiply_button.click(
        inputs=[a, b],
        outputs=[c]
    )
    def multiply(x, y):
        return x * y
    
    @divide_button.click(
        inputs=[a, b],
        outputs=[c]
    )
    def divide(x, y):
        if y == 0:
            return "除數不能為零"
        return x / y
    
demo.launch()