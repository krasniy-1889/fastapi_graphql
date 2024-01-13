from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Base


class SQLAlchemyRepository:
    model = None | Base

    def __init__(self, session: AsyncSession):
        self.session = session
