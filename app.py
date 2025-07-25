import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY environment variable not set")

# Configure the Gemini client
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

app = FastAPI(title="Office Chat")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    try:
        result = model.generate_content(req.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return ChatResponse(response=result.text)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
