from typing import Union

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    username = ''
    return templates.TemplateResponse("home.html", {
        "request": request,
        "username": username,
    })