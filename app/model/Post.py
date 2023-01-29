from dataclasses import dataclass

from app.model.PublicUser import PublicUser


@dataclass
class Post:
    id: int
    img_url: str
    author: PublicUser | None = None
    text: str | None = None
