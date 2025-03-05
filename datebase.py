from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DB_URL = "sqlite+aiosqlite:///DateBase.db"

Engine = create_async_engine(DB_URL)
Session = async_sessionmaker(Engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


async def create_all_tables():
    async with Engine.begin() as connection:
        await connection.run_sync(Model.metadata.create_all)

async def delete_all_tables():
    async with Engine.begin() as connection:
        await connection.run_sync(Model.metadata.drop_all)