from sqlalchemy import select, update, delete, func
from datebase import Session
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
    except:
        return {"status": "Error", "message": "Incorrect format"}


async def get_account(account: schems.UserGet):
    try:
        async with Session() as session:

            user: models.User = await session.scalar(select(models.User).where(models.User.tgID == account.tgID))
            if user:
                return {"id": user.id, "name": user.Name, "surname": user.Surname, "secondname": user.SecondName}
            return {"status": "Error", "message": "User not in DB"}
    except:
        return {"status": "Error", "message": "User not in DB"}



async def add_task(task: schems.Task):
    try:
        async with Session() as session:
            data = task.model_dump()
            task = models.Task(**data)

            session.add(task)
            await session.commit()
            return {'status': 'ok'}
    except:
        return {"status": "Error", "message": "Incorrect format"}

async def set_completed_task(task_get: schems.TaskSet):
    try:
        async with Session() as session:
            task: models.Task = session.scalar(select(models.Task).where(models.Task.id == task_get.taskID, models.Task.userID == task_get.userID))
            if task:
                task.completed = task_get.completed
                await session.refresh(task)
                await session.commit()
                return {"status": "ok"}
            return {"status": "invalid-user", "message": "this user has no access rights"}
    except:
        return {"status": "invalid-user", "message": "this user has no access rights"}