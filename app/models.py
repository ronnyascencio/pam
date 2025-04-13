import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    full_name: str = Field(max_length=40)
    username: str = Field(min_length=3, max_length=10)
    email: EmailStr


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserRegister(SQLModel):
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=8, max_length=40)
    full_name: str | None = Field(default=None, max_length=255)


class User(UserBase, table=True):
    id: uuid.UUID | None = Field(default=None, primary_key=True)
    hashed_password: str


""" meta data """


class Meta(SQLModel, table=True):
    camera: str
    lens: str
    date: str | None = Field(default=None)
    author: str | None = Field(default=None, foreign_key="user.full_name")


""" collections """


class Collection(SQLModel, table=True):
    collection_name: str
    category: str
    user_id: uuid.UUID | None = Field(default=None, foreign_key="user.id")


""" Items  content"""


class Item(SQLModel, table=True):
    title: str
    user_id: uuid.UUID | None = Field(default=None, foreign_key="user.id")
    description: str | None = Field(default=None, max_length=255)
    medadata: str | Meta | None = Field(default=None)
    collection_id: str | None = Field(
        default=None, foreign_key="collection.collection_name"
    )
