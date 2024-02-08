import datetime
from db.models import User
from schemas import UserBase, SearchBase
from sqlalchemy.orm import Session
from db.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status
from db.models import Whois
import http.client
import json

def create_user(request: UserBase, db: Session):
    user = User(
        username = request.username,
        password = Hash.bcrypt(request.password),
        email = request.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete_user(request: UserBase, db:Session):

    user = db.query(User).filter(User.username == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid credential')

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid password')

    db.delete(user)
    db.commit()
    return user

def getAll(db:Session):
    result = db.query(User).all()
    return result

def get(id: int, db:Session):
    result = db.query(User).filter(User.id == id).first()
    return result