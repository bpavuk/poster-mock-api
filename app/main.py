from datetime import timedelta, datetime
from typing import List

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import BaseModel
from starlette import status
from app.data.poster_data import users_dict, pwd_context, posts, users
from app.model.Post import Post
from app.model.PublicUser import PublicUser
from app.model.Response import Response
from app.model.User import User
from app.secrets.secrets import SECRET_KEY

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# DATA
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


# UTILITIES
def get_fake_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return user_dict


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_fake_user(users_dict, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user.to_public_user()


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def authenticate_user(fake_db, username: str, password: str):
    user = get_fake_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# ENDPOINTS

@app.get("/users/me")
async def read_users_me(current_user: PublicUser = Depends(get_current_user)):
    return current_user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(users_dict, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.user_name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    return posts[post_id]


@app.get("/posts")
async def get_posts(start: int = 0, limit: int = 5, username: str | None = None):
    filtered_posts: List[Post] = []

    for i in range(len(posts)):
        if posts[i].author.user_name == username or username is None:
            filtered_posts.append(posts[i])

    for i in range(len(filtered_posts)):
        if filtered_posts[i].id == start or start == 0:
            return filtered_posts[i:min(i + limit, len(filtered_posts) - 1)]


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    for i in range(len(users)):
        if users[i].id == user_id:
            return users[i].to_public_user()

    raise HTTPException(status_code=404, detail="User not found")


@app.post("/posts/new")
def publish_post(post: Post, current_user: User = Depends(get_current_user)) -> Response:
    for i in posts:
        if i.id == post.id:
            raise HTTPException(status_code=406, detail="Post with same ID exists")

    post.author = current_user.to_public_user()

    posts.append(post)
    return Response(state="Success")
