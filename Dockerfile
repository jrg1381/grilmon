FROM python:3.6

EXPOSE 5000
ADD requirements.txt /requirements.txt
ADD Makefile /src/Makefile
ADD fakebin/killall /usr/bin/killall
RUN pip install -r /requirements.txt
WORKDIR /src

CMD make run_network
