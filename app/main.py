from transformers import pipeline
question_answerer = pipeline("question-answering", model="consciousAI/question-answering-roberta-base-s")
from fastapi import FastAPI, Form
from typing_extensions import Annotated
app = FastAPI()
@app.post("/qa/")
async def QA(question: Annotated[str, Form()],context: Annotated[str, Form()]):
    answer=question_answerer(question=question, context=context)
    return {"Answer": answer["answer"]}


