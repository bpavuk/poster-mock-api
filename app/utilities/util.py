def fake_hash_password(password: str):
    return password + "Fuck"


def get_fake_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return user_dict
