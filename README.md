# Markdown server with Flask

Simple markdown server written with Flask.

**You can read this README in a structured manner if you run the server.**

## Content management

This is a simple content management system that uses Flask and Markdown to serve content from a directory. The content is written in Markdown and converted to HTML on the fly.

### Routing

Routes are defined by the file structure in the `content` directory. The content of the page is found in the current directory's `index.md` file.

[Route example](content_management/route_example)

### Meta data

Optional meta data can be added in the markdown file in frontmatter format. The only required field is `title`, this is used as the page title.

```markdown
---
title: Page title
---
```

## Route example

This markdown is placed in the `content/content_management/route_example/index.md` path.

The file tree looks like:

```shell
.
└── content
    └── content_management
        ├── index.md
        └── route_example
            └── index.md
```

Compare this path to the URL: `/content_management/route_example`.

## Styling

For styling <a href="https://matcha.mizu.sh/" target="__blank">matcha.css</a> is used. It is a simple and clean classless CSS framework.

## Development

This project needs Python 3.11 or newer to run. Development was done in classic virtual environment (venv).

All useful commands are in the Makefile.

### Installation

Set up the virtual environment and install the dependencies in said environment with pip.

```bash
make dev-build
```

### Running

Run the `dev-build` target than run the Flask server.

```bash
make dev-run
```

### Testing

Run the tests in virtual environment.

```bash
make dev-test
```

### Project structure

There is one package in the project: `markdown_server`. It is registered as a blueprint in the main Flask app.

The **action-domain-responder** pattern is organized in python module named by their responsibility. For example there is a `domain.py` module wich holds methods for reading the markdown files, and generating html as content.

## Containerization

The application can be containerized with Docker. The Dockerfile is in the root of the project.

The relevant commands are in the Makefile.

### Building the image

```bash
make build
```

### Running the container

```bash
make run
```

## Running Tests

Run the `build` target than run the tests in the container.

```bash
make test
```

### Stopping the container

```bash
make stop
```

### Removing all the associated containers and images

```bash
make clean
```

Since we can chain make targets, setting up would be `make build run` and tearing down would be `make stop clean`.
