from fastapi import FastAPI

from data.poster_data import posts

app = FastAPI()


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    return posts[post_id]


@app.get("/posts")
def get_posts(start: int, limit: int = 5):
    return posts[start:min(start + limit, len(posts))]
