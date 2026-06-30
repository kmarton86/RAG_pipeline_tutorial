from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "answer": None
        }
    )


@app.post("/", response_class=HTMLResponse)
def ask_question(request: Request, question: str = Form(...)):

    answer = f"Ezt kérdezted: {question}"

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "answer": answer
        }
    )