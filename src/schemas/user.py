from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]


class User(UserCreate):
    id: int
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    registration_date: datetime
