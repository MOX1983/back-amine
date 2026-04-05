from sqlalchemy.orm import Session

from models import User

import bcrypt


def getUsers(db: Session):
    return db.query(User).all()

def getUser(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def updateUser(db: Session, user: User):
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


def createUser(db: Session, user: User):
    user = User(email=user.email, name=user.name, password=bcrypt.hashpw(bytes(user.password, 'utf-8'),  bcrypt.gensalt()))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

