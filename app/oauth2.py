from jose import JWSError, jwt
from datetime import datetime, timedelta
from . import schemas, database, postmodel
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

#SECRET_KEY
SECRET_KEY = settings.secret_key
# Algorithm 
ALGORITHM = settings.algorithm
# Expiration Time
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_endcode = data.copy()
    # setup expire time
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_endcode.update({"exp": expire})
    # create jwt token
    jwt_token = jwt.encode(to_endcode, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token


def verify_access_token(token: str, credential_exception):
    try:
        print("payload")
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        print(payload)
        id: str = payload.get("user_id")
        
        if id is None:
            raise credential_exception
        token_data = schemas.TokenData(id = id)
        print({"token data is": token_data})
    except JWSError:
        print("exception occurred")
        raise credential_exception
    
    return token_data

    
def get_current_user(token: str = Depends(oauth2_scheme), db = Depends(database.get_db)):
    credential_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, 
        detail = f"Couldn't validate credential", headers={"WWW-Authenticate": "Bearer"})
    token = verify_access_token(token, credential_exception)
    user = db.query(postmodel.User).filter(postmodel.User.id == token.id).first()
    print("User is")
    print(user.id)
    return user
           
    