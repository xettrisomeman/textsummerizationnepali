from pathlib import Path

from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware import cors

from model import get_summarized_text, get_text


origins = [
    'http://127.0.0.1:8000',
    'http://0.0.0.0:8000'
]

import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")


app.add_middleware(cors.CORSMiddleware, allow_origin=orgins, allow_credentials=True, allow_methods = ["*"])


@app.get("/")
def read_root():
    return {"message": "Go to /models"}



@app.get("/models", response_class=HTMLResponse)
def predict(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})



@app.post('/models', response_class=HTMLResponse)
def predict(request: Request, input_text: str = Form(...)):
    summarized_sentence, original_text = get_summarized_text(input_text)
    return templates.TemplateResponse("index.html", context={"request": request, "summary": summarized_sentence, "original_text": original_text})




