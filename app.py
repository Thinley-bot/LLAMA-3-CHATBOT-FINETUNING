import requests 
import json
import gradio as gr

url="http://localhost:11434/api/generate"

headers={
    'Content-Type': 'application/json'
}

history = []

def generate(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)
    data = {
        "model": "lopen",
        "prompt": final_prompt,
        'stream': False
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response)
    
    if response.status_code == 200:
        response = response.text
        data=json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        return "Error: " + str(response.status_code)

interface = gr.Interface(
    fn=generate,
    inputs=gr.Textbox(lines=4, label="Enter your prompt"),
    outputs="text",
)
interface.launch()