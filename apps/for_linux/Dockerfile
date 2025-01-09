FROM python:3.12.8-alpine3.20

RUN mkdir ./app

COPY requirements.txt  /app/
COPY app.py /app/

RUN python -m pip install -r /app/requirements.txt

