FROM python:3.9-slim

RUN apt-get update && apt-get install -y make && apt-get install -y curl

RUN mkdir /code
COPY . /code/
WORKDIR /code

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH "$PATH:/root/.poetry/bin"
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction
