import torch
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

model_dir = './model/blenderbot_mentalhealth_finetuned'

import os
print("Model folder contents:", os.listdir(model_dir))

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = BlenderbotTokenizer.from_pretrained(model_dir)
model = BlenderbotForConditionalGeneration.from_pretrained(model_dir).to(device)
model.eval()

print(f"Model loaded on {device}")

print("Start chatting with the bot! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Exiting chat.")
        break
    inputs = tokenizer(user_input, return_tensors='pt', padding=True, truncation=True, max_length=128).to(device)
    with torch.no_grad():
        generated_ids = model.generate(
            **inputs,
            max_new_tokens=64,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.8
        )
    response = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    print(f"Bot: {response}")
# model_dir = './model/blenderbot_mentalhealth_finetuned'

# import os
# print("Model folder contents:", os.listdir(model_dir))
