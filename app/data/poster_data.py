from random import choice
from typing import Mapping
from passlib.context import CryptContext
from app.data.fakes import fake
from app.model.Post import Post
from app.model.User import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


users: list[User] = [
    User(
        id=i,
        profile_img=f"{fake.image_url()}",
        user_name=f"{fake.user_name()}",
        hashed_password=pwd_context.hash("fuckery")
    ) for i in range(10)
]

for i in users:
    print(i.user_name)
    print(i.hashed_password)

users_dict: Mapping[str, User] = { i.user_name : i for i in users  }

posts: list[Post] = [
    Post(
        id=i,
        author=choice(users).to_public_user(),
        img_url=f"{fake.image_url()}",
        text=f"{fake.paragraph()}"
    ) for i in range(100)
]
