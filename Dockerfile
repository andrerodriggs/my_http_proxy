# syntax=docker/dockerfile:1
FROM python:3.8
LABEL maintainer="als.rodrigues@gmail.com"
LABEL version="1.0"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .
