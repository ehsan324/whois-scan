from pydantic import BaseModel
from datetime import datetime
from typing import List


class UserBase(BaseModel):
    username: str
    password: str
    email: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True


class UserAuth(BaseModel):
    username: str
    password: str


class SearchBase(BaseModel):
    domain_name: str
    APIKey: str
    user_id: int
    token: str


class SearchDisplay(BaseModel):
    domain_name: str
    user_id: int
    result: dict

    class Config:
        from_attributes = True
