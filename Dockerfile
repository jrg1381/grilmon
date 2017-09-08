FROM python:3.6

EXPOSE 5000
RUN apt-get update && apt-get install -y dh-virtualenv
ADD requirements.txt /requirements.txt
ADD Makefile /src/Makefile
ADD fakebin/killall /usr/bin/killall
RUN pip install -r /requirements.txt
WORKDIR /src

CMD tail -f /dev/null
