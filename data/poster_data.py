from typing import List

from data.fakes import fake
from model.Post import Post

posts: List[Post] = [
    Post(
        author_id=0,
        img_url=f"{fake.image_url()}",
        text=f"{fake.paragraph()}"
    ),
    Post(
        author_id=1,
        img_url=f"{fake.image_url()}",
        text=f"{fake.paragraph()}"
    ),
    Post(
        author_id=0,
        img_url=f"{fake.image_url()}",
        text=f"{fake.paragraph()}"
    ),
]
