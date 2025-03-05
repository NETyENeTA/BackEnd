from fastapi import APIRouter

from sqlalchemy.sql.annotation import Annotated
from fastapi.params import Depends
from typing import Annotated

import schems
import requests as rq

userRoute = APIRouter(prefix="/api/user")

@userRoute.post("/add")
async def add_user(
        user: Annotated[schems.User, Depends()]
):
    return await rq.add_account(user)

@userRoute.get("/get")
async def add_user(
        user: Annotated[schems.UserGet, Depends()]
):
    return await rq.get_account(user)

taskRoute = APIRouter(prefix="/api/task")

@taskRoute.post('/add')
async def add_task(
        task: Annotated[schems.Task, Depends()]
):
    return await rq.add_task(task)

@taskRoute.patch('/completed')
async def set_completed_task(
        task: Annotated[schems.TaskSet, Depends()]
):
    return await rq.set_completed_task(task)