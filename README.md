# poster-mock-api
Mock api for https://github.com/bpavuk/poster-android

# How to start server?

  Firstly create secrets folder in app package. Then create secrets.py fle in it. This one may store variable SECRET_KEY which you can generate using command below
  ```
  openssl rand -hex 32
  ```
  It's preferred to use Dockerfile for building a Docker image. After building just run image and don't forget to bind container port 80 to system port 3001

# Where I can get OpenAPI specification?

  Start server and go to localhost:3000/openapi.json. Then copy-paste specification to your desired SwaggerUI tool
