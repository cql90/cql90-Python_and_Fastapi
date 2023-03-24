from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import database, schemas, postmodel, utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=["authentication"])

# @router.post('/login')
# def login(user_credentials: schemas.UserLogin, db = Depends(database.get_db)):
#     user = db.query(postmodel.User).filter(postmodel.User.email == user_credentials.email).first()
    
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Invalid Credential')
    
#     if not utils.verify_password(user_credentials.password, user.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Invalid Credential')
    
#     access_token = oauth2.create_access_token(data = {"user_id": user.id})
#     return {"access_token": access_token, "token_type": "bearer"}

@router.post('/login', response_model = schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db = Depends(database.get_db)):
    user = db.query(postmodel.User).filter(postmodel.User.email == user_credentials.username).first()
    print(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f'Invalid Credential')
    
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f'Invalid Credential')
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}