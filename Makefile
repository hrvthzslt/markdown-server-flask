.PHONY: help
.DEFAULT_GOAL := help

IMAGE_TAG := markdown_server
PORT := 8000
VENV_NAME := env

help:
	@grep -h -E '^[a-zA-Z0-9_-]+:.*?# .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: # Build the docker image
	docker build -t $(IMAGE_TAG) .

.PHONY: run
run: # Run the docker image
	docker run -d -p $(PORT):8000 $(IMAGE_TAG)

.PHONY: stop
stop: # Stop the docker container
	docker stop $$(docker ps -q --filter ancestor=$(IMAGE_TAG))

.PHONY: clean
clean: # Remove all related docker images and containers
	docker rm $$(docker ps -a -q --filter ancestor=$(IMAGE_TAG))
	docker rmi $(IMAGE_TAG)

.PHONY: test
test: build # Run the unit tests in container
	docker run -it $(IMAGE_TAG) bash -c "python -m unittest discover -s test/unit/"

VENV=env
PYTHON=$(VENV)/bin/python3

.PHONY: dev-build
dev-build: # Create a virtual environment and install the dependencies
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements.txt

.PHONY: dev-run
dev-run: dev-build # Run the server in the virtual environment
	$(PYTHON) -m flask run --debug -p $(PORT)

.PHONY: dev-stop
dev-test: # Run the unit tests in the virtual environment
	$(PYTHON) -m unittest discover -s test/unit/
