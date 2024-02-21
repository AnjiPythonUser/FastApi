from pydantic import BaseModel
from typing import List
class Child(BaseModel):
    name: str
    last_name: str
    age: int

class Person(BaseModel):
    name: str
    age: int
    childs: List[Child]
