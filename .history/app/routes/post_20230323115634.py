from typing import List, Optional
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Response
from ..database import engine, session, get_db
from .. import postmodel, schemas, oauth2
from sqlalchemy import func

router = APIRouter(
    prefix="/posts",
    tags=['posts']
)

postmodel.Base.metadata.create_all(bind = engine)



def test_post():
    post = session.query(postmodel.Post).all()
    print(post)
    return {"Data": post}



# get all post by matching user id
# @router.get("/", response_model=List[schemas.PostResponse]) 
@router.get("/", response_model=List[schemas.PostResponseExt ]) 
def get_post(db = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
             limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    print(search)
    post_query = db.query(postmodel.Post).filter(postmodel.Post.user_id == current_user.id).filter(postmodel.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    result = db.query(postmodel.Post, func.count(postmodel.Vote.post_id).label('Vote')).join(postmodel.Vote, 
                    postmodel.Vote.post_id == postmodel.Post.id, 
                    isouter=True).group_by(postmodel.Post.id).all()
    print(result)
    return post_query


# get post by id
@router.get("/{id}", response_model=schemas.PostResponse)
def get_post(id: int, db = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_item = db.query(postmodel.Post).filter(postmodel.Post.user_id == current_user.id).filter(postmodel.Post.id == id).first()
    if not post_item:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} not found")
    return post_item


# This is add new data to database 
# @router.post("/", status_code = status.HTTP_201_CREATED, response_model=schemas.Post)
@router.post("/", status_code = status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(post: schemas.PostCreate, db = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_post = postmodel.Post(user_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
 


# # delete post from database
@router.delete("/{id}", status_code = status.HTTP_200_OK)
def delete_post(id: int, db = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    print("Current user id")
    print(current_user.id)
    post_query = db.query(postmodel.Post).filter(postmodel.Post.id == id)
    delete_post_item = post_query.first()
    if delete_post_item == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} not found")
    if delete_post_item.user_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = f"Not authorize to perform delete.")
    post_query.delete(synchronize_session = False)
    db.commit()
    return Response(status_code = status.HTTP_200_OK)



# update post from database
# @router.put("/{id}", status_code = status.HTTP_200_OK, response_model=schemas.Post)
@router.put("/{id}", status_code = status.HTTP_200_OK, response_model=schemas.PostResponse)
def update_post(id: int, update_post: schemas.PostCreate, db = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    print("Current user id")
    print(current_user.id)
    update_item = db.query(postmodel.Post).filter(postmodel.Post.id == id)
    updatepost = update_item.first()
    if updatepost == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} not found")
    if updatepost.user_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = f"Not authorize to perform delete.")
    update_item.update(update_post.dict(), synchronize_session = False)
    db.commit()
    return update_item.first()