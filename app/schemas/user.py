import datetime
from uuid import UUID

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    password: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    sid: UUID
    created_at = datetime.datetime
    updated_at = datetime.datetime

    class Config:
        orm_mode = True
