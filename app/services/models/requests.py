from pydantic import BaseModel, EmailStr


class UserSignupRequest(BaseModel):
    email: EmailStr
    name: str
    surname: str
    password: str


class UserSigninRequest(BaseModel):
    email: EmailStr
    password: str
