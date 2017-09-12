FROM python:3.6-stretch

RUN apt-get update && apt-get install -y dh-virtualenv debhelper
RUN pip3 install setuptools
ADD . /src
WORKDIR /src

CMD tail -f /dev/null