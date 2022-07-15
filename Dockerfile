FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN sudo apt-get install awscli
RUN python -m pip install --upgrade pip

RUN python -m pip install -r requirements.txt

COPY ./app /app
