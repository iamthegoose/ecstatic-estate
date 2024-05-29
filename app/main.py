from fastapi import FastAPI, Depends, Form, Response, Request
from fastapi.templating import Jinja2Templates
import logging
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from sqlalchemy.orm import Session
from app.services.connection import SessionFactory

from app.services.security import get_password_hash, verify_password, create_access_token, COOKIE_NAME

# repository
from app.repositoryuser import UserRepository

# types
from app.services.models.user import User

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/front/static",
          html=True), name="static")

template = Jinja2Templates("app/front/html")

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root(request: Request):
    return template.TemplateResponse(request, "index.html")


@app.get("/login")
def login(request: Request):
    return template.TemplateResponse(request, "login.html")


@app.get("/signup")
def signin(request: Request):
    return template.TemplateResponse(request, "registration.html")


@app.post("/user/signup")
def signup_user(email: str = Form(), name: str = Form(), surname: str = Form(), password: str = Form()):
    print(name)
    print(surname)
    print(email)
    print(password)
    with SessionFactory() as sess:
        userRepository = UserRepository(sess)
        db_user = userRepository.get_user_by_email(email)
        if db_user:
            return "User with such email already exists"

        signup = User(email=email, name=name, surname=surname,
                      password=get_password_hash(password))
        success = userRepository.create_user(signup)


@app.post("/user/signin")
def signin_user(response: Response, email: str = Form(), password: str = Form()):
    with SessionFactory() as sess:
        userRepository = UserRepository(sess)
        db_user = userRepository.get_user_by_email(email)
        if not db_user:
            return "User with such email doesn't exist "

        if verify_password(password, db_user.password):
            token = create_access_token(db_user)
            response.set_cookie(
                key=COOKIE_NAME,
                value=token,
                httponly=True,
                expires=1800
            )
            return {COOKIE_NAME: token, "token_type": "goose"}
        return {"дабайоб"}


logging.basicConfig(level="DEBUG")
