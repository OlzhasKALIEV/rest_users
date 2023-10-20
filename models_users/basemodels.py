from pydantic import BaseModel


class Users(BaseModel):
    name: str
    surname: str
    patronymic: str


class UserUpdate(BaseModel):
    name: str
    surname: str
    patronymic: str
    age: int
    gender: str
    nationality: str
