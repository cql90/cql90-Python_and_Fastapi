from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from ..database import engine, get_db
from .. import postmodel, schemas, utils

router = APIRouter(
    prefix= "/users",
    tags=['users']
)

postmodel.Base.metadata.create_all(bind = engine)

@router.post("/", status_code = status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db = Depends(get_db)):
    hash_password = utils.hash(user.password)
    user.password = hash_password
    new_user = postmodel.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# get user after login
@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db = Depends(get_db)):
    user_item = db.query(postmodel.User).filter(postmodel.User.id == id).first()
    if not user_item:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"user with id: {id} not found")
    return user_item