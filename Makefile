FLASK_DEBUG=1
FLASK_APP=grilmon/main.py

.PHONY: run
run:
	flask run

.PHONY: run_network
run_network:
	flask run --host=0.0.0.0

.PHONY: container
container:
	docker-compose up --build

build:
	python setup.py sdist
