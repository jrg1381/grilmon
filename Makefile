run:
	FLASK_APP=grilmon/main.py flask run

run_network:
	FLASK_APP=grilmon/main.py flask run --host=0.0.0.0

build:
	python setup.py sdist
