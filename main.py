import uvicorn
from fastapi import FastAPI

from contextlib import asynccontextmanager
from datebase import create_all_tables, delete_all_tables

from routers import userRoute, taskRoute

@asynccontextmanager
async def life_span(app: FastAPI):
    await delete_all_tables()
    print("Tables was cleaned!")
    await create_all_tables()
    print("Base is Ready to [work]")
    yield
    print("Saving\nStatus: Off")

app = FastAPI(lifespan=life_span)
app.include_router(userRoute)
app.include_router(taskRoute)

# if __name__ == '__main__':
#     uvicorn.run('main:app', reload=True)