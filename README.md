# poster-mock-api
Mock api for https://github.com/bpavuk/poster-android

# How to start server?
Just clone this repository, install dependencies from requirements.txt and start server using command below
```
pip install -r requirements.txt
uvicorn main:app --reload
```

# Where I can get OpenAPI specification?

Start derver and go to localhost:3000/openapi.json. Then copy-paste specification to your desired SwaggerUI tool
