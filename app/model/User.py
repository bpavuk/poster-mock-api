from dataclasses import dataclass


@dataclass
class User:
    user_name: str
    profile_img: str
    id: int
    hashed_password: str

    def to_public_user(self):
        from app.model.PublicUser import PublicUser
        return PublicUser(
            id=self.id,
            user_name=self.user_name,
            profile_img=self.profile_img
        )
