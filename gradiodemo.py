import gradio as gr
from openai import OpenAI
import os


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat(message: str,history):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message['text']}
            ]
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(e)
        return {"error": str(e)}



# Create the Gradio interface
demo = gr.ChatInterface(
    fn=chat, 
    multimodal=True,
    title="Chatbot POC",
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
