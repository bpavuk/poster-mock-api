from dataclasses import dataclass
from typing import Union

from model.User import User


@dataclass
class Post:
    id: int
    author: User
    img_url: str
    text: Union[str, None] = None
