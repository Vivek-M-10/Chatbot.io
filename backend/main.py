from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot import ask_gemini

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Gemini Chat API is running!"}

@app.post("/chat/")
def chat_with_gemini(request: PromptRequest):
    response = ask_gemini(request.prompt)
    if response.startswith("❌"):
        raise HTTPException(status_code=500, detail=response)
    return {"response": response}
