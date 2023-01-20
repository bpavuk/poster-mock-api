from typing import List

from data.fakes import fake
from model.Post import Post

posts: List[Post] = [
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
