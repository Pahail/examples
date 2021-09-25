from pydantic import Field, BaseModel, validator, ValidationError
from typing import List, Optional


class UserModel(BaseModel):
    name: str
    password: str

    @validator('password')
    def password_validation(cls, v):
        if len(v) < 6:
            raise ValidationError("Password should contain at least 6 symbols")
        return v
