from sqlalchemy.orm import Mapped, mapped_column

from datebase import Model

class User(Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tgID: Mapped[int]

    Name: Mapped[str]
    Surname: Mapped[str]
    SecondName: Mapped[str]



class Task(Model):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(primary_key=True)
    userID: Mapped[int]

    title: Mapped[str]
    completed: Mapped[bool] = False