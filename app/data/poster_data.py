from random import choice

from app.data.fakes import fake
from app.model.Post import Post
from app.model.User import User

users: list[User] = [
    User(
        id=i,
        profile_img=f"{fake.image_url()}",
        user_name=f"{fake.user_name()}"
    ) for i in range(5)
]


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
