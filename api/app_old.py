import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Mental Health Chatbot API")

# Enable CORS middleware (update allowed_origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model directly from Hugging Face Hub
model_dir = "AnupSarkarDD/blenderbot-mentalhealth-finetuned"
print(f"Loading model from: {model_dir}")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load tokenizer and model from Hugging Face Hub
tokenizer = BlenderbotTokenizer.from_pretrained(model_dir)
model = BlenderbotForConditionalGeneration.from_pretrained(model_dir)
model.to(device)
model.eval()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat/")
async def chat(request: ChatRequest):
    user_input = request.message
    if not user_input.strip():
        raise HTTPException(status_code=400, detail="Empty message provided.")

    inputs = tokenizer(
        user_input, return_tensors="pt", padding=True, truncation=True, max_length=128
    ).to(device)

    with torch.no_grad():
        generated_ids = model.generate(
            **inputs,
            max_new_tokens=64,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.8,
        )
    response = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return {"response": response}
