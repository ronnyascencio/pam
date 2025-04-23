import uuid
from typing import Annotated

from database import engine
from fastapi import APIRouter, Depends
from models import User
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from sqlmodel import Field, Session
from starlette import status

""" Hasshed password"""


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# bcrypt.__about__ = bcrypt


""" Session Db"""


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


router = APIRouter(prefix="/users", tags=["users"])

""" Healthy check """


@router.get("/user_healthy")
async def user_healthy_check():
    return {"status": "healthy"}


""" Models """


class UserBaseRegister(BaseModel):
    full_name: str
    username: str = Field(min_length=4)
    email: EmailStr
    password: str = Field(min_length=6)


""" User CRUD"""


@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def user_register(base_register: UserBaseRegister, session: SessionDep):
    user_model = User(
        id=uuid.uuid4(),
        full_name=base_register.full_name,
        username=base_register.username,
        email=base_register.email,
        hashed_password=bcrypt_context.hash(base_register.password),
    )
    session.add(user_model)
    session.commit()
    session.refresh(user_model)
    return user_model


@router.get("/all/", status_code=status.HTTP_200_OK)
async def read_all_users(session: SessionDep) -> list[User]:
    return session.exec(User).all()
