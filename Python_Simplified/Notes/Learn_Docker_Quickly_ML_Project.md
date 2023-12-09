## 1. Containers

- Containers use the same hardwareas our operating system.
- However, they are separated entities that operate in a sandbox.
- Therefore all software requirements are pre-installed inside containers.

## 2. Why Containers?

- With containers, we can work on the same environment from different computers.

## 3. Images

- Docker images are similar to GitHub Repositories. 
- But instead of software - they store environments where software is installed.
- Docker images have a read-only format.
- We can build new images, but we can't change existing ones. We can think of images as a static set of instructions. We use them to create containers.
- Containers are running instances of images. Unlike images, we can change and interact with them.

## 4. Docker Practice

- In cmd window, write `docker search jupyter`
- `docker pull jupyter/tensorflow-notebook`
- `docker run -p 8000:8888 jupyter/tensorflow-notebook`

## 5. Docker Compose

## 6. Mount Drive

## 7. Dockerfile

## 8. Prune Containers

- `docker container prune`