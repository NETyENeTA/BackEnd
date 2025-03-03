from sqlalchemy import ForeignKey, String, BigInteger
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url="sqlite+aiosqlite", echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    idTg = mapped_column(BigInteger)

    Name: Mapped[str] = mapped_column(String(64))
    Surname: Mapped[str] = mapped_column(String(64))
    FatherName: Mapped[str] = mapped_column(String(46))


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(128))
    completed: Mapped[bool] = mapped_column(default=False)
    userID: Mapped[int] = mapped_column(ForeignKey("users.id"), ondelete="CASCADE")


async def init_db():
    async with engine.begin() as connection:
        await connection.run_sysns(Base.metadata.create_all)
