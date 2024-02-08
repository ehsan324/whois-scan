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

SECRET_KEY = 'b50b06cf039958cccde65c14829f856de03b1621f4ab3e7621b9782492c4ec9a'


def whois_search(request: SearchBase, db: Session):
    if request.token == SECRET_KEY:
        conn = http.client.HTTPSConnection("api.whoisfreaks.com")
        payload = json.dumps({"domainNames": [request.domain_name]})
        headers = {'Content-Type': 'application/json'}
        conn.request("POST", f"/v1.0/bulkwhois?apiKey={request.APIKey}", payload, headers)
        res = conn.getresponse()
        data = json.loads(res.read().decode('utf-8'))
        search = Whois(
            domain_name=request.domain_name,
            APIKey=request.APIKey,
            timestamp=datetime.datetime.now(),
            result=data,
            user_id=request.user_id,
        )
        db.add(search)
        db.commit()
        db.refresh(search)
        return search
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="please enter correct access token")
