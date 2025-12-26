from typing import Type
from pydantic import BaseModel


class Task(BaseModel):
    name: str
