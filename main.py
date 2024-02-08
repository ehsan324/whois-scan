from fastapi import FastAPI
from router import user
from db.database import Base, engine
from auth import authentication
from router import whois


app = FastAPI()
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(whois.router)

Base.metadata.create_all(engine)

@app.get('/wellcome')
def wellcome():
    return 'wellcome'