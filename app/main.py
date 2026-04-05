from models import User

from sqlalchemy import select

from sqlalchemy.orm import sessionmaker, Session
from database import engine

Session = sessionmaker(bind=engine)
db = Session()

try:
    users = db.execute(select(User)).scalars().all()
    print(users)
finally:
    db.close()
