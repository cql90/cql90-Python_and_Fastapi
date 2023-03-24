from typing import List, Optional
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Response
from ..database import engine, session, get_db
from .. import postmodel, schemas, oauth2

router = APIRouter(
    prefix="/votes",
    tags=['Vote']
)

postmodel.Base.metadata.create_all(bind = engine)