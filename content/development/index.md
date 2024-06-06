---
title: "Development"
---

# Development

This project needs Python 3.11 or newer to run. Development was done in classic virtual environment (venv).

All useful commands are in the Makefile.

## Installation

Set up the virtual environment and install the dependencies in said environment with pip.

```bash
make dev-build
```

## Running

Start the Flask server in the virtual environment in debug mode.

```bash
make dev-run
```

## Testing

Run the tests in virtual environment.

```bash
make dev-test
```

## Project structure

There is one package in the project: `markdown_server`. It is registered as a blueprint in the main Flask app.

The **action-domain-responder** pattern is organized in python modules named by their responsibility. For example there is a `domain.py` module wich holds methods for reading the markdown files, and generating html as content.

[Back](/)
