from fastapi import FastAPI

app = FastAPI(title="Enterprise Knowledge Copilot")

@app.get("/health")
def health():
    return {"status": "ok"}