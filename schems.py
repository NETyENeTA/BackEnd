
from pydantic import BaseModel

class UserGet(BaseModel):
    tgID: int


class User(UserGet):
    Name: str
    Surname: str
    SecondName: str

class TaskGet(BaseModel):
    userID: int

class TaskDelete(BaseModel):
    id: int

class Task(TaskDelete):
    title: str



