from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import UserDisplay, UserBase, UserAuth
from db.database import get_db
from db import db_user
import http.client



router = APIRouter(prefix='/user', tags=['user'])

@router.post('/create',response_model=UserDisplay)
def create_user(request: UserBase, db:Session = Depends(get_db)):
    return db_user.create_user(request, db)

@router.post('/delete', response_model=UserDisplay)
def delete_user(request: UserAuth, db: Session = Depends(get_db)):
    return db_user.delete_user(request, db)

@router.get('/getall')
def getAll(db:Session=Depends(get_db)):
    return db_user.getAll(db)

@router.get('/get/{id}',response_model=UserDisplay)
def get(id:int, db:Session=Depends(get_db)):
    return db_user.get(id, db)