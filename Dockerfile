FROM python:3.6

EXPOSE 5000
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
WORKDIR /src

CMD tail -f /dev/null
