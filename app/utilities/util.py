from app.data.poster_data import users_dict


def fake_hash_password(password: str):
    return password + "Fuck"


def get_fake_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return user_dict


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_fake_user(users_dict, token)
    return user
