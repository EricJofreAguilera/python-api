
from pydantic import BaseModel, EmailStr, Field
from typing import List
from datetime import datetime

class Phone(BaseModel):
    number: int
    citycode: int
    contrycode: int

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phones: List[Phone]
