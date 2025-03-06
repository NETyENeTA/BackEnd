from sqlalchemy import select, update, delete, func
from datebase import Session, QUOTES
from random import randint as rnd
import schems
import models


async def add_account(account: schems.User):
    try:
        async with Session() as session:
            data = account.model_dump()
            account = models.User(**data)

            session.add(account)
            await session.commit()
            return {'status': 'ok'}
    except Exception as e:
        return {"status": "critical-error", "message": e}


async def get_account(account: schems.UserGet):
    try:
        async with Session() as session:

            user: models.User = await session.scalar(select(models.User).where(models.User.tgID == account.tgID))
            if user:
                return {"id": user.id, "name": user.Name, "surname": user.Surname, "secondname": user.SecondName}
            return {"status": "Error", "message": "User not in DB"}
    except:
        return {"status": "Error", "message": "User not in DB"}

async def get_tasks(task: schems.TaskGet):
    try:
        async with Session() as session:
            tasks: list[models.Task] = await session.scalars(select(models.Task).where(models.Task.userID == task.userID))

            if len(tasks) != 0 and tasks:
                formatted = []
                for task in tasks:
                    formatted.append({"title": task.title})
                return {tasks: formatted}
            return {"status": "error", "message": "user is indefined"}
    except Exception as e:
        return {"status": "critical-error", "message": e}


async def add_task(task: schems.Task):
    try:
        async with Session() as session:
            data = task.model_dump()
            task = models.Task(**data)

            session.add(task)
            await session.commit()
            return {'status': 'ok'}
    except:
        return {"status": "Error", "message": f"Incorrect format"}

async def del_task(task_del: schems.TaskDelete):
    try:
        async with Session() as session:
            task: models.Task | None = await session.scalar(select(models.Task).where(models.Task.id == task_del.id))
            if task:
                session.delete(task)
                await session.commit()
                return {"status": "ok"}
            return {"status": "error", "message": "task id is out in massive"}
    except Exception as e:
        return {"status": "critical-error", "message": e}

async def get_quote():
    return QUOTES[rnd(0, len(QUOTES) - 1)]
