from fastapi import APIRouter

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

@taskRoute.get('/get')
async def get_tasks(
        task: Annotated[schems.TaskGet, Depends()]
):
    return await rq.get_tasks(task)

@taskRoute.post('/add')
async def add_task(
        task: Annotated[schems.Task, Depends()]
):
    return await rq.add_task(task)

@taskRoute.delete('/delete')
async def del_task(
        task: Annotated[schems.TaskDelete, Depends()]
):
    return await rq.del_task(task)

apiRoute = APIRouter(prefix="/api")

@apiRoute.get("/quote")
async def get_quote():
    quote, name = await rq.get_quote()
    return {"quote": quote, "name": name}
