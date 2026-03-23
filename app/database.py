from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

from setting import setting
import asyncio

engine = create_async_engine(url=setting.get_db_url(), echo=True)

SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession)

Base = declarative_base()

