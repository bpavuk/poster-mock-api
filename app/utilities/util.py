from fastapi import HTTPException, Depends
from starlette import status

from app.data.poster_data import users_dict
from app.main import oauth2_scheme, pwd_context


def fake_hash_password(password: str):
    return password + "Fuck"


def get_fake_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return user_dict


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_fake_user(users_dict, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
