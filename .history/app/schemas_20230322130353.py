from pydantic import BaseModel, EmailStr
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
    create_at: d
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


class UserCreate(BaseModel):
    email: EmailStr
    password: str


# class UserResponse(BaseModel):
#     id: int
#     email: EmailStr
    
#     class Config:
#         orm_mode = True


class UserLogin(BaseModel):   
    email: EmailStr
    password: str  


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
          
   