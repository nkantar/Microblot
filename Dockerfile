FROM python:3.8-slim

RUN apt-get update && apt-get install -y make

RUN mkdir /code
COPY . /code/
WORKDIR /code

RUN pip install poetry
RUN poetry install --no-root
