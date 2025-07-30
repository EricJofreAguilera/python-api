
from pydantic import BaseModel, EmailStr, Field
from typing import List
from datetime import datetime

class Phone(BaseModel):
    number: str
    citycode: str
    contrycode: str

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phones: List[Phone]
