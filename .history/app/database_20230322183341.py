from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<user_name>:<password>@<ip-address/hostname>/<database_name>'

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Kurt9a$kate@localhost/Python_and_Fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
SessionLocal = Session()

Base = declarative_base()

def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close_all() 