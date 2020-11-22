FROM python:3.8-alpine

LABEL language="python"
LABEL framework="flask"
LABEL usage="hello-world"

RUN apk update && apk add --no-cache py3-gunicorn
RUN addgroup flask && adduser -h /var/local/helloworld -D -G flask flask

USER flask
WORKDIR /var/local/helloworld

RUN pip3 install --upgrade --no-warn-script-location --disable-pip-version-check pip && \
    pip3 install --no-warn-script-location flask==1.1.2

COPY --chown=flask helloworld .
RUN python3 setup.py install --user

COPY --chown=flask docker-command.sh .
RUN chmod +x docker-command.sh

RUN mkdir ./logs
ADD logging.conf .

EXPOSE 5000

ENV FLASK_ENV="production" FLASK_DEBUG="false" 
ENV TLS_CERTIFICATE="" TLS_KEY=""

CMD ["./docker-command.sh"]
