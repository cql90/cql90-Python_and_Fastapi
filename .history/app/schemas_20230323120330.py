from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass   


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    create_at: datetime
    class Config:
        orm_mode = True
        
        
# this class will handle the response 
class PostResponse(BaseModel):
    id: int
    create_at: datetime
    user_id: int
    owner: UserResponse
    class Config:
        orm_mode = True   


class PostResponseExt(PostBase):
    post: PostResponse
    votes: int        


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):   
    email: EmailStr
    password: str  


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None

# le mean less then or equal to 1
class Vote(BaseModel):
    post_id: int
    direction: conint(le=1)
          
   