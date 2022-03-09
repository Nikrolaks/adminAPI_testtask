from datetime import date, datetime
from enum import Enum
from pydantic import BaseModel


class UserRole(str, Enum):
    ADMIN = 'admin'
    PREMIUM_USER = 'premium'
    BASE_USER = 'base'


class User(BaseModel):
    id: int
    registration_date: date
    last_login: datetime
    age: int
    role: UserRole
    login: str
    password: str

    class Config:
        orm_mode = True
