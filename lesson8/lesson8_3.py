## Block 架構

import gradio as gr



with gr.Blocks() as demo:  # block區塊
    name_textbox = gr.Textbox(label='姓名', placeholder='請輸入姓名')
    output_texbox = gr.Textbox(label='輸出', placeholder='輸出結果會顯示在這裡')
    greet_button = gr.Button('打招呼')

    @greet_button.click(
        inputs = [name_textbox],
        outputs = [output_texbox]
    )
    def greet(name):
        return name + '你好!'


demo.launch()