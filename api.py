from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import predict_sentiment

class TextInput(BaseModel):
    text: str

app = FastAPI()

@app.post("/predict_sentiment/")
def process_text(input: TextInput):
    try:
        result = predict_sentiment(input.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
