from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import SearchBase, SearchDisplay
from db.database import get_db
from db import db_whois
import http.client

router = APIRouter(prefix='/whois', tags=['whois'])


@router.post('/search', response_model=SearchDisplay)
def whois_search(request: SearchBase, db: Session = Depends(get_db)):
    return db_whois.whois_search(request, db)
