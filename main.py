from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    name: str
    age: int
    publish: bool = True
    school: Optional[str] = None


@app.get("/")
def root():
    return {"message": "Hello Faraz, how are you"}

@app.get("/post")
def get_post():
    return {"data": "Your post is updated"}

@app.post("/")
def post_data(insta: Post = Body(...)):
    print(insta.name)
    return {"new_post": f"{insta.name} {insta.age}"}

@app.post("/base")
def data(new_post: Post):
    # print(new_post)
    print(new_post.dict())
    return {"data": "new post"}


