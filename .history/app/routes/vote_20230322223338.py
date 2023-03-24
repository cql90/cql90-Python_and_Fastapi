from typing import List, Optional
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Response
from ..database import engine, session, get_db
from .. import postmodel, schemas, oauth2

router = APIRouter(
    prefix="/votes",
    tags=['Vote']
)

postmodel.Base.metadata.create_all(bind = engine)

@router.post("/", status_code = status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # make sure the post exist first
    post = db.query(postmodel.Post).filter(postmodel.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail= f"user {current_user.id} has already voted on post {vote.post_id}")
    vote_query = db.query(postmodel.Vote).filter(postmodel.Vote.post_id == vote.post_id, postmodel.Vote.user_id == current_user.id)
    found_vote = vote_query.first()

    if(vote.direction == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                                detail= f"user {current_user.id} has already voted on post {vote.post_id}")
        new_vote = postmodel.Vote(post_id = vote.post_id, user_id = current_user.id)    
        db.add(new_vote)
        db.commit()
        return {"Message": "Successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Vote didn't existed")    
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"Message": "Successfully deleted  vote"}