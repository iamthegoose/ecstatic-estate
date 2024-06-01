from fastapi import FastAPI, Depends, Form, Response, Request
from fastapi.templating import Jinja2Templates
import logging
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from sqlalchemy.orm import Session
from app.services.connection import SessionFactory

from app.services.security import get_password_hash, verify_password, create_access_token, COOKIE_NAME

# repository
from app.repositoryuser import UserRepository

# types & models
from app.services.models.user import User
from app.services.models.requests import UserSigninRequest, UserSignupRequest

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/front/static",
          html=True), name="static")

templates = Jinja2Templates(directory="app/front/html")

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
def index_file(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/login")
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/signup")
def signup(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})


@app.get("/rent")
def signup(request: Request):
    return templates.TemplateResponse("flats.html", {"request": request})


@app.get("/create-flats")
def signup(request: Request):
    return templates.TemplateResponse("create-flats.html", {"request": request})

# @app.post("/user/signup")
# def signup_user(request:Request, email: str = Form(None), name: str = Form(None), surname: str = Form(None), password: str = Form(None)):
#     if not email or not password or not name or not surname:
#         return templates.TemplateResponse("registration.html", {"request": request, "message": "Заповніть всі поля!"})
#     with SessionFactory() as sess:
#         userRepository = UserRepository(sess)
#         db_user = userRepository.get_user_by_email(email)
#         if db_user:
#             return templates.TemplateResponse("registration.html", {"request": request, "message": "Користувач з такою поштою вже існує!"})

#         signup = User(email=email, name=name, surname=surname, password=get_password_hash(password))
#         success = userRepository.create_user(signup)
#         return templates.TemplateResponse("registration.html", {"request": request, "message": "Користувач створений успішно"})


@app.post("/user/signup")
def signup_user(user_request: UserSignupRequest, request: Request):
    if not user_request.email or not user_request.password or not user_request.name or not user_request.surname:
        return templates.TemplateResponse("registration.html", {"request": request, "message": "Заповніть всі поля!"})

    with SessionFactory() as sess:
        userRepository = UserRepository(sess)
        db_user = userRepository.get_user_by_email(user_request.email)

        if db_user:
            return templates.TemplateResponse("registration.html", {"request": request, "message": "Користувач з такою поштою вже існує!"})

        signup = User(
            email=user_request.email,
            name=user_request.name,
            surname=user_request.surname,
            password=get_password_hash(user_request.password)
        )
        success = userRepository.create_user(signup)

        # Генеруємо токен після успішного створення користувача
        token = create_access_token(sess, user_request.email)

        return {"token": token, "message": "Користувач створений успішно"}


@app.post("/user/signin", response_class=JSONResponse)
def signin_user(user_request: UserSigninRequest, request: Request):
    with SessionFactory() as sess:
        userRepository = UserRepository(sess)
        db_user = userRepository.get_user_by_email(user_request.email)
        if not db_user:
            return JSONResponse(status_code=400, content={"message": "Користувача з такою поштою не існує!"})

        if verify_password(user_request.password, db_user.password):
            token = create_access_token(sess, user_request.email)
            return {"token": token, "message": "Успішний вхід"}

        return JSONResponse(status_code=400, content={"message": "Неправильний пароль!"})


@app.get("/success", response_class=HTMLResponse)
def success_page(request: Request, token: str):
    return templates.TemplateResponse("index.html", {"request": request, "token": token})


logging.basicConfig(level="DEBUG")
