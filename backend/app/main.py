from fastapi import FastAPI

app = FastAPI(title="Budget Reimagined", version="0.0.1")

@app.get("/")
async def health():
    return {
        "health": "ok"
    }
    
