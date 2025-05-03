# Docker activity

1. Initialize Git: `git init`
2. Create `app.py` and type the code.
3. Create a `Dockerfile` to containerize the app.
4. Start a local Docker registry: `docker run -d -p 5000:5000 --name registry registry:2`
5. Build the Docker image: `docker build -t localhost:5000/demo .`
6. Push the image to the registry: `docker push localhost:5000/demo`
7. Run the container with an environment variable: `docker run -e secret_user=<your_name> localhost:5000/demo`
