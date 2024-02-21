from typing import Union
from schemas import Person
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sum")
def read_item(value1: int, value2: int):
    return {
        "value1": value1,
        "value2": value2,
        "result": value1 + value2
    }


@app.post("/person")
def read_root(person: Person):
    return person