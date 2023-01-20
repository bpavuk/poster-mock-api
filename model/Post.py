from dataclasses import dataclass
from typing import Union


@dataclass
class Post:
    id: int
    author_id: int
    img_url: str
    text: Union[str, None] = None
