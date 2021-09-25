from pydantic import Field, BaseModel
from typing import List, Optional


class User(BaseModel):
    name: str
    password: str
