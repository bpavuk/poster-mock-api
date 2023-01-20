from dataclasses import dataclass
from typing import Union


@dataclass
class Post:
    author_id: int
    img_url: str
    text: Union[str, None] = None


post = Post(author_id=0, img_url="fuckery", text="Hello Fuckery")
