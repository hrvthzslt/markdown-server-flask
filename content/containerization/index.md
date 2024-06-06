---
title: "Containerization"
---

# Containerization

The application can be containerized with Docker. The Dockerfile is in the root of the project.

The relevant commands are in the Makefile.

## Building the image

```bash
make build
```

## Running the container

```bash
make run
```

## Running Tests

Run the tests in the container.

```bash
make test
```

## Stopping the container

```bash
make stop
```

## Removing all the associated containers and images

```bash
make clean
```

---

Since we can chain make targets, setting up would be `make build run` and tearing down would be `make stop clean`.

[Back](/)
