from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker

from setting import setting
import asyncio

engine = create_async_engine(url=setting.get_db_url(), echo=True)

SessionLocal = sessionmaker(bind=engine, class_=AsyncSession)

Base = declarative_base()

async def get_db():
    async with SessionLocal() as db:
        yield db

