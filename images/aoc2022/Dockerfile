FROM python:3.8-slim-buster

RUN pip install --upgrade pip

ENV PYTHONPATH "${PYTHONPATH}:/"

WORKDIR /input/

COPY ./src/common /common
COPY ./src/aoc2022 /aoc2022
COPY ./input/ /input/


ENV WORKDIR=/input

CMD [ "python", "-m", "aoc2022" ]