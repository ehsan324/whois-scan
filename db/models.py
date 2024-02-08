from db.database import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from typing import List

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    search = relationship("Whois", back_populates='user')

class Whois(Base):
    __tablename__ = "Search"

    id = Column(Integer, primary_key=True, index=True)
    domain_name = Column(String)
    APIKey = Column(String)
    timestamp = Column(DateTime)
    result = Column(JSON)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='search')

