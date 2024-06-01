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

test: build
	docker run -it $(IMAGE_TAG) bash -c "python -m unittest discover -s test/unit/"

VENV=env
PYTHON=$(VENV)/bin/python3

dev-build:
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements.txt

dev-run: dev-build
	$(PYTHON) -m flask run --debug -p $(PORT)

dev-test:
	$(PYTHON) -m unittest discover -s test/unit/
