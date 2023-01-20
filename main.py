from fastapi import FastAPI

from data.poster_data import posts

app = FastAPI()


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    return posts[post_id]


@app.get("/posts")
def get_posts(start: int = 0, limit: int = 5):
    for i in range(len(posts)):
        if posts[i].id == start or start == 0:
            return posts[i:i + limit]
