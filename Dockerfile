FROM python:3.8-alpine

LABEL language="python"
LABEL framework="flask"
LABEL usage="hello-world"

RUN addgroup flask && adduser -h /var/local/helloworld -D -G flask flask && \
  mkdir /usr/local/helloworld && chown flask:flask /usr/local/helloworld

#RUN pip3 install --upgrade --disable-pip-version-check pip
RUN pip3 install gunicorn==20.0.4
COPY --chown=flask helloworld /usr/local/helloworld/
RUN cd /usr/local/helloworld/ && pip3 install -r requirements.txt && python3 setup.py install

COPY --chown=root:flask docker-command.sh /
RUN chmod og+x /docker-command.sh

WORKDIR /var/local/helloworld

RUN mkdir ./logs && chown flask:flask ./logs
COPY --chown=flask logging.conf .

EXPOSE 5000
EXPOSE 5443

ENV FLASK_ENV="production" FLASK_DEBUG="false" 
ENV TLS_CERTIFICATE="" TLS_KEY=""

USER flask
CMD ["/docker-command.sh"]
