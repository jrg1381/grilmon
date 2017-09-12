FLASK_DEBUG=1
FLASK_APP=grilmon/main.py
DOCKER_EXEC=docker-compose exec web
BUILDER=docker-compose exec builder


.PHONY: run_network
run_network:
	flask run --host=0.0.0.0

.PHONY: run
run: container
	$(DOCKER_EXEC) make run_network

.PHONY: container
container:
	docker-compose up --build -d

package: container
	$(BUILDER) dpkg-buildpackage -us -uc

build:
	python setup.py sdist
