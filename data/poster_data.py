
from data.fakes import fake
from model.Post import Post
from model.User import User

posts: list[Post] = [
    Post(
        id=24,
        author_id=0,
        img_url=f"{fake.image_url()}",
        text=f"{fake.paragraph()}"
    ),
    Post(
        id=365,
        author_id=1,
        img_url=f"{fake.image_url()}",
        text=f"{fake.paragraph()}"
    ),
    Post(
        id=89,
        author_id=0,
        img_url=f"{fake.image_url()}",
        text=f"{fake.paragraph()}"
    ),
]

users: list[User] = [
    User(
        id=i,
        profile_img=f"{fake.image_url()}",
        user_name=f"{fake.user_name()}"
    ) for i in range(5)
]
