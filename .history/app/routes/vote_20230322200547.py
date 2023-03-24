from typing import List, Optional
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Response
from ..database import engine, session, get_db
from .. import postmodel, schemas, oauth2, Vote

router = APIRouter(
    prefix="/votes",
    tags=['Vote']
)

postmodel.Base.metadata.create_all(bind = engine)

@router.post("/", status_code = status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(post: schemas.PostCreate, db = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_post = postmodel.Vote(user_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post