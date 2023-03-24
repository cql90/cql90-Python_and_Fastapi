from typing import List, Optional
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Response
from ..database import engine, session, get_db
from .. import postmodel, schemas, oauth2

router = APIRouter(
    prefix="/votes",
    tags=['Vote']
)

postmodel.Base.metadata.create_all(bind = engine)

@router.post("/", status_code = status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(vote: schemas.Vote, db = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    vote_query = db.query(postmodel.Vote).filter(postmodel.Vote.id == vote.post_id, postmodel.Vote.user_id == current_user.id)
    if(vote.direction == 1):
        
    else:
            