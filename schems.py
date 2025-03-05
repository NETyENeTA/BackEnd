
from pydantic import BaseModel

class UserGet(BaseModel):
    tgID: int


class User(UserGet):
    Name: str
    Surname: str
    SecondName: str

class TaskSet(BaseModel):
    userID: int
    taskID: int
    completed: bool

class Task(BaseModel):
    userID: int
    title: str



