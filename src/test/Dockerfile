FROM python:3.9.7-slim-buster

RUN pip install --upgrade pip && \
  pip install -U pytest pytest-cov

ENV PYTHONPATH "${PYTHONPATH}:/"

COPY ./src/test /test
COPY ./src/common /common
COPY ./src/aoc2022 /aoc2022
COPY ./src/aoc2023 /aoc2023
COPY ./src/test/conftest.py /conftest.py

ENTRYPOINT [ "pytest","--cov-config", "/test/.coveragerc", "--cov", "-p", "no:cacheprovider", "/test" ]
