from dataclasses import dataclass


@dataclass
class PublicUser:
    user_name: str
    profile_img: str
    id: int
