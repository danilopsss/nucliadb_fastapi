FROM python:3.10-slim as basic-build

COPY pyproject.toml .
COPY scripts/start.sh .

RUN apt update && \
    apt install iputils-ping -y

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install


FROM basic-build as main_app
WORKDIR /app
COPY scripts/ .
COPY main_api main_api
CMD ["sh", "-c", "/app/start.sh API nuclia_db"]

FROM basic-build as test_step
WORKDIR /app
COPY main_api main_api
COPY test test
CMD ["pytest", "-v", "test"]

