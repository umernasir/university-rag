from fastapi import FastAPI
from pydantic import BaseModel
from ragservice import askquestion


app = FastAPI()
class Question(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(request: Question):
    answer, sources = askquestion(request.question)
    return {
        "answer": answer,
        "sources": list(sources)
    }

