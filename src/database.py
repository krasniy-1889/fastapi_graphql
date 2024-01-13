from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import config


class Base(DeclarativeBase):
    pass


engine = create_async_engine(
    url=config.DB_URL,
    echo=True,
    pool_size=10,
    max_overflow=10,
)

async_session_maker = async_sessionmaker(engine)
