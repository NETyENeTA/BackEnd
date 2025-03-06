from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

QUOTES = [
    ("Что разум человека может постигнуть и во что он может поверить, того он способен достичь", "Наполеон Хилл"),
    ("Стремитесь не к успеху, а к ценностям, которые он дает", "Альберт Эйнштейн"),
    ("Своим успехом я обязана тому, что никогда не оправдывалась и не принимала оправданий от других.", "Флоренс Найтингейл"),
    ("Сложнее всего начать действовать, все остальное зависит только от упорства.", "Амелия Эрхарт")
]

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
