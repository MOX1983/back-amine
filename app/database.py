from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

from setting import setting

engine = create_engine(url=setting.get_db_url(), echo=True)

Base = declarative_base()

def create_db_and_tables() -> None:
	Base.metadata.create_all(engine)


