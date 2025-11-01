import gradio as gr
import torch
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# MODEL LOAD
model_dir = "AnupSarkarDD/blenderbot-mentalhealth-finetuned"
tokenizer = BlenderbotTokenizer.from_pretrained(model_dir)
model = BlenderbotForConditionalGeneration.from_pretrained(model_dir)
model.eval()

def bot_reply(message, history):
    inputs = tokenizer(message, return_tensors="pt", padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        generated_ids = model.generate(**inputs, max_new_tokens=64)
    response = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return response

# Use only one main heading via title param, give plain friendly note in description
with gr.ChatInterface(
    fn=bot_reply,
    title="🧠 AI Mental Health Chatbot",
    description="Speak openly—your conversation stays private. Powered by Blenderbot.",
    theme="huggingface",  # Better theme for visibility than "soft"
    examples=["I'm feeling stressed lately", "How can I sleep better?", "I'm addicted to my phone", "Hi, how are you?"],
    ) as demo:
    pass

if __name__ == "__main__":
    demo.launch()
