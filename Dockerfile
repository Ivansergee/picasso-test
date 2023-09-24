FROM python:3.10-alpine3.18

COPY requirements.txt /temp/requirements.txt
COPY uploader /uploader
WORKDIR /uploader
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password picasso

USER picasso
