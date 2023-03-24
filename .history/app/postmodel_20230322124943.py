from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, relationship
from sqlalchemy.sql.expression import text, relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
from pydantic import BaseModel
from typing import Optional

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, nullable=False) 
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=False)
    create_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey('users.id', ondelete ='CASCADE'), nullable=False)
    owner = relationship("users")

class User(Base):
    __tablename__ = 'users' 
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    create_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
 