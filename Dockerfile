# syntax=docker/dockerfile:1.3

FROM python:3.10

WORKDIR /src/server

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache \
    pip install --no-cache-dir -r requirements.txt

COPY . /src/server

EXPOSE 50053