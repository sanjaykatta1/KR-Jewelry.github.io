from typing import Union

from fastapi import FastAPI

app = FastAPI()

chambers = []

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/post")
def post_item(data):
    chambers.append(data)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}