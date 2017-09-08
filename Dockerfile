FROM python:3.6

EXPOSE 5000
ADD grilmon/requirements.txt /requirements.txt
ADD Makefile /src/Makefile
RUN pip install -r /requirements.txt
WORKDIR /src

CMD make run_network
