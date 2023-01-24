from dataclasses import dataclass


@dataclass
class User:
    user_name: str
    profile_img: str
    id: int
    hashed_password: str
