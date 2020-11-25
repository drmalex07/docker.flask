# vim: set syntax=dockerfile:
FROM python:3.8-alpine

COPY helloworld/requirements.txt helloworld/requirements-testing.txt ./
RUN pip3 install -r requirements.txt -r requirements-testing.txt

ENV FLASK_ENV="testing" FLASK_DEBUG="false" 
