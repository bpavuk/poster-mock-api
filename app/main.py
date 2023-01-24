from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from app.data.poster_data import posts, users, users_dict
from app.model.Post import Post
from app.model.Response import Response
from app.model.User import User
from app.utilities.util import fake_hash_password, get_current_user

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@app.post("/token")
async def login(form_data:OAuth2PasswordRequestForm = Depends()):
    user = users_dict.get(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.user_name, "token_type": "bearer"}


@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    return posts[post_id]


@app.get("/posts")
async def get_posts(start: int = 0, limit: int = 5):
    for i in range(len(posts)):
        if posts[i].id == start or start == 0:
            return posts[i:i + limit]


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    for i in range(len(users)):
        if users[i].id == user_id:
            return users[i]

    raise HTTPException(status_code=404, detail="User not found")


@app.post("/posts/new")
def publish_post(post: Post) -> Response:
    for i in posts:
        if i.id == post.id:
            raise HTTPException(status_code=406, detail="Post with same ID exists")

    posts.append(post)
    return Response(state="Success")
