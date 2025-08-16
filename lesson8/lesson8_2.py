## Block 架構

import gradio as gr

def greet(name):
    return name + '你好!'

with gr.Blocks() as demo:  # block區塊
    name_textbox = gr.Textbox(label='姓名', placeholder='請輸入姓名')
    output_texbox = gr.Textbox(label='輸出', placeholder='輸出結果會顯示在這裡')
    greet_button = gr.Button('打招呼')

    greet_button.click(fn=greet,
                       inputs = [name_textbox],
                       outputs = [output_texbox])


demo.launch()