FROM python:3.8-slim-buster

RUN pip install --upgrade pip && \
  pip install pytest && \
  pip install pytest-cov

ENV PYTHONPATH "${PYTHONPATH}:/"

WORKDIR /work/

COPY ./src/test /test
COPY ./src/common /common
COPY ./src/aoc2022 /aoc2022
COPY ./src/aoc2023 /aoc2023
COPY ./src/test/conftest.py /conftest.py

ENV WORKDIR=/test/input

ENTRYPOINT [ "pytest","--cov-config", "/test/.coveragerc", "--cov", "-p", "no:cacheprovider", "/test" ]
