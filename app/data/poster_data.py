from random import choice
from typing import Mapping

from app.data.fakes import fake
from app.model.Post import Post
from app.model.User import User

users: list[User] = [
    User(
        id=i,
        profile_img=f"{fake.image_url()}",
        user_name=f"{fake.user_name()}",
        hashed_password=f"{fake.password()}" + "Fuck"
    ) for i in range(5)
]

for i in users:
    print(i.user_name)
    print(i.hashed_password)

users_dict: Mapping[str, User] = { i.user_name : i for i in users  }


posts: list[Post] = [
    Post(
        id=24,
        author=choice(users),
        img_url=f"{fake.image_url()}",
        text=f"{fake.paragraph()}"
    ),
    Post(
        id=365,
        author=choice(users),
        img_url=f"{fake.image_url()}",
        text=f"{fake.paragraph()}"
    ),
    Post(
        id=89,
        author=choice(users),
        img_url=f"{fake.image_url()}",
        text=f"{fake.paragraph()}"
    ),
]
