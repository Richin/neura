from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import uvicorn

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ollama API settings
OLLAMA_API = "http://localhost:11434/api/generate"
MODEL_NAME = "deepseek-r1:1.5b"

class AnalysisRequest(BaseModel):
    url: str
    content: str

@app.post("/analyze")
async def analyze_webpage(request: AnalysisRequest):
    try:
        # Prepare the prompt
        prompt = f"""
        Analyze the following content for misinformation, bias, and credibility.
        - Assign a trust score (0-100) where 100 is highly trustworthy.
        - Highlight potential fake news, bias, or manipulation.
        - Identify key sources, tones, and any misleading elements.

        URL: {request.url}
        Content: {request.content[:8000]}
        """
        
        # Call Ollama API
        response = requests.post(
            OLLAMA_API,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Analysis service unavailable")
            
        analysis = response.json().get("response", "No analysis generated.")
        
        return {
            "success": True,
            "trust_score": "75",  # This should be extracted from the analysis
            "analysis": analysis
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 