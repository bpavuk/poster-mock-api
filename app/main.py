from fastapi import FastAPI, HTTPException

from app.data.poster_data import posts, users
from app.model.Post import Post
from app.model.Response import Response

app = FastAPI()


@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    return posts[post_id]


@app.get("/posts")
async def get_posts(start: int = 0, limit: int = 5):
    for i in range(len(posts)):
        if posts[i].id == start or start == 0:
            return posts[i:i + limit]


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    for i in range(len(users)):
        if users[i].id == user_id:
            return users[i]

    raise HTTPException(status_code=404, detail="User not found")


@app.post("/posts/new")
def publish_post(post: Post) -> Response:
    for i in posts:
        if i.id == post.id:
            raise HTTPException(status_code=406, detail="Post with same ID exists")

    posts.append(post)
    return Response(state="Success")
