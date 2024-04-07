from typing import Union

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from db_conn import conn

templates = Jinja2Templates(directory="templates")

app = FastAPI()

# Pydantic model to define the schema of the data
class Post(BaseModel):
    title: str
    description: str = None


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    username = ''
    return templates.TemplateResponse("home.html", {
        "request": request,
        "username": username,
    })

@app.get("/post/{post_id}", response_model=Post)
async def read_post(post_id: int):
    cursor = conn.cursor()
    query = "SELECT id, title, description FROM posts WHERE id=%s"
    cursor.execute(query, (post_id,))
    post = cursor.fetchone()
    cursor.close()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"id": post[0], "title": post[1], "description": post[2]}


# Run Application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=5432)
# In command line
# uvicorn main:app --host 0.0.0.0 --port 5432