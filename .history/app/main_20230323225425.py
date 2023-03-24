from fastapi import FastAPI
from .routes import post, user, auth, vote
from .config import settings
from fastapi.middleware import CORM

app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get('/')
def root():
    return {"Message": "Hello World"}