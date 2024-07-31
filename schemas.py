from uuid import UUID
from pydantic import BaseModel, Field
from fastapi import Query

class TokenSchema(BaseModel):
    access_token: str = Query(None, regex="^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$")


class SuccessLogin(BaseModel):
    username: str
    token: str = Query(None, regex="^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$")
    status: bool
    msg: str

class FailLogin(BaseModel):
    username: str
    status: bool
    msg: str

class TokenPayload(BaseModel):

    sub: str = None
    exp: int = None


class UserAuth(BaseModel):
    username: str = Field(..., description="username")
    password: str = Field(..., min_length=5, max_length=24, description="user password")


class UserOut(BaseModel):
    id: UUID
    email: str


class SystemUser(UserOut):
    password: str