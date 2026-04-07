from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer

from models import User
from crud import *
from schemes import User as UserScheme, UserBase, UserLogin
from auth import create_token, verify_token

from sqlalchemy.orm import sessionmaker, Session
from database import engine, Base

Base.metadata.create_all(engine)
app = FastAPI()

Session = sessionmaker(bind=engine)
db = Session()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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

@app.get("/")
def get_all(db: Session = Depends(get_db)):
    return getUsers(db)

@app.post("/create")
def create_user(user: UserBase, db: Session = Depends(get_db)):
    return createUser(db, user)

@app.post("/token")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = findUserByEmail(db, data.email)

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if bcrypt.checkpw(data.password.encode("utf-8"), user.password.encode("utf-8")):
        access_token = create_token(data={"sub":user.name})
        return {"access_token": access_token,
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email
                }}
    raise HTTPException(status_code=400, detail="Invalid credentials")
