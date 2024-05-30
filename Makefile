IMAGE_TAG := markdown_server
PORT := 8000
VENV_NAME := env

build:
	docker build -t $(IMAGE_TAG) .

run:
	docker run -d -p $(PORT):8000 $(IMAGE_TAG)

stop:
	docker stop $$(docker ps -q --filter ancestor=$(IMAGE_TAG))

clean:
	docker rm $$(docker ps -a -q --filter ancestor=$(IMAGE_TAG))
	docker rmi $(IMAGE_TAG)

VENV=env
PYTHON=$(VENV)/bin/python3

dev:
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m flask run --debug -p $(PORT)
