# 建立一個gradio的Blocks的架構
# 功能:
# 1. 建立姓名輸入框
# 2. 建立輸出框
# 3. 建立按鈕

import gradio as gr
import os
from google import genai


with gr.Blocks() as demo:  # block區塊
    input_textbox = gr.Textbox(label='輸入', placeholder='請輸入')
    output_texbox = gr.Textbox(label='輸出', placeholder='輸出結果會顯示在這裡')
    greet_button = gr.Button('送出')  # 按鈕
    @greet_button.click(
        inputs = [input_textbox],
        outputs = [output_texbox])
    def ai_client(output):
        # 使用Google Gemini AI客戶端
        # 請確保已經設定好環境變數 GEMINI_API_KEY
        if 'GEMINI_API_KEY' not in os.environ:
            raise ValueError("請設定環境變數 GEMINI_API_KEY")
        # 建立Google Gemini AI客戶端
        # 使用環境變數中的API金鑰
        client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])
        # 呼叫AI模型生成內容
        # 使用模型名稱 "gemini-2.5-flash"
        # 並將輸入內容傳遞給模型
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=output
        )
        return response.text


demo.launch()