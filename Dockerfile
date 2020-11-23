FROM python:3.6

LABEL language="python"
LABEL framework="flask"
LABEL usage="hello-world"

RUN apt-get update
RUN groupadd -r flask && useradd -r -g flask -m -d /var/local/helloworld flask
RUN pip3 install --upgrade --no-warn-script-location --disable-pip-version-check pip

USER flask
WORKDIR /var/local/helloworld

COPY --chown=flask wsgi.py .
RUN chmod +x wsgi.py

COPY --chown=flask helloworld .
RUN pip3 install -r requirements.txt && python3 setup.py install --user

RUN mkdir ./logs
COPY --chown=flask logging.conf .

EXPOSE 5000

ENV FLASK_ENV="production" FLASK_DEBUG="false" 
ENV TLS_CERTIFICATE="" TLS_KEY=""

CMD ["/var/local/helloworld/wsgi.py"]
