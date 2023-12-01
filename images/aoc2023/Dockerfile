FROM python:3.8-slim-buster

RUN pip install --upgrade pip

ENV PYTHONPATH "${PYTHONPATH}:/"

WORKDIR /input/

COPY ./src/common /common
COPY ./src/aoc2023 /aoc2023
COPY ./input/ /input/


ENV WORKDIR=/input

CMD [ "python", "-m", "aoc2023" ]