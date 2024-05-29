from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from fastapi import Depends, Request
from app.settings import settings

from app.services.models.user import User

ACCESS_TOKEN_EXPIRE_MINUTES = 3000

pwd_context = CryptContext(
    schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")
COOKIE_NAME = "Authorization"

# create Token


def create_access_token(user):
    try:
        payload = {
            "email": user.email,
            "role": user.role.value,
        }
        return jwt.encode(payload, key=settings.JWT_SECRET.get_secret_value(), algorithm=settings.ALGORITHM.get_secret_value())
    except Exception as ex:
        print(str(ex))
        raise ex

# create verify Token


def verify_token(token):
    try:
        payload = jwt.decode(token, key=settings.JWT_SECRET.get_secret_value())
        return payload
    except Exception as ex:
        print(str(ex))
        raise ex

# password hash


def get_password_hash(password):
    return pwd_context.hash(password)

# password verify


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_current_user_from_token(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    return user


def get_current_user_from_cookie(request: Request) -> User:
    token = request.cookies.get(COOKIE_NAME)
    if token:
        user = verify_token(token)
        return user
