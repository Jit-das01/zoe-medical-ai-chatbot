from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    message: str
    session_id: str = None

@app.get("/")
def root():
    return {"message": "ZOE AI is running", "status": "healthy"}

@app.get("/api/health")
def health():
    return {"status": "healthy"}

@app.post("/api/chat")
def chat(request: ChatRequest):
    try:
        print(f"Received message: {request.message}")
        print(f"API Key present: {openai.api_key is not None}")
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are ZOE, a helpful medical assistant."},
                {"role": "user", "content": request.message}
            ],
            temperature=0.7,
            max_tokens=300
        )
        
        bot_response = response.choices[0].message['content']
        
        return {
            "response": bot_response,
            "session_id": request.session_id or f"session_{datetime.now().timestamp()}",
            "is_emergency": False,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {
            "error": f"OpenAI API Error: {str(e)}",
            "response": f"Sorry, I encountered an error: {str(e)}"
        }

if __name__ == "__main__":
    import uvicorn
    print("\n🤖 ZOE Medical AI starting...")
    print(f"📍 API Key loaded: {openai.api_key[:20]}..." if openai.api_key else "❌ No API key found!")
    uvicorn.run(app, host="0.0.0.0", port=8000)
