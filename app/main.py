from fastapi import FastAPI
from fastapi.params import Depends

from models import User
from crud import createUser

from sqlalchemy.orm import sessionmaker, Session
from database import engine

app = FastAPI()

Session = sessionmaker(bind=engine)
db = Session()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

user = User()
user.name = 'mox'
user.email = 'mox@gmail.com'
user.password = '123123'

def create_user(user: User, db: Session = Depends(get_db)):
    return createUser(db, user)

print(create_user(user, db))