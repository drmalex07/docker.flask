# vim: set syntax=dockerfile:
FROM python:3.8-alpine

RUN apk update && apk add --no-cache g++ gcc musl-dev libc-dev python3-dev

COPY helloworld/requirements.txt helloworld/requirements-testing.txt ./
RUN pip3 install -r requirements.txt -r requirements-testing.txt

ENV FLASK_ENV="testing" FLASK_DEBUG="false" 
