from fastapi import FastAPI, HTTPException

from data.poster_data import posts, users

app = FastAPI()


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    return posts[post_id]


@app.get("/posts")
def get_posts(start: int = 0, limit: int = 5):
    for i in range(len(posts)):
        if posts[i].id == start or start == 0:
            return posts[i:i + limit]


@app.get("/user/{user_id}")
def get_user(user_id: int):
    for i in range(len(users)):
        if users[i].id == user_id:
            return users[i]

    raise HTTPException(status_code=404, detail="User not found")
