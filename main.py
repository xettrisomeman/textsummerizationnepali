from pathlib import Path

from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

from app import get_summarized_text, get_text


app = FastAPI()

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))


@app.get("/")
def read_root():
    return {"message": "Go to /models"}


@app.get("/models", response_class=HTMLResponse)
def read_item(request: Request, input_text: str = Form(...)):
    text_file = get_summarized_text(input_text)
    return templates.TemplateResponse("index.html", context={"request": request, "text": text_file})


