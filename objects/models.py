from typing import Optional

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    userId: str
    userName: str
    phoneNumber: str


    