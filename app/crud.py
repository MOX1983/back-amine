from sqlalchemy.orm import Session

from models import User
from schemes import User as UserScheme, UserBase

import bcrypt


def getUsers(db: Session):
    return db.query(User).all()

def getUser(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def updateUser(db: Session, user: UserBase):
    db.query(User).filter(User.id == user.id).update(user.to_dict())
    db.commit()
    db.refresh(user)
    return user

def deleteUser(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).delete()
    db.commit()
    db.refresh(user)
    return user

def findUserByEmail(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def findUserById(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def createUser(db: Session, user: UserBase):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    user = User(email=user.email, name=user.name, password=hashed_password.decode("utf-8"))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

