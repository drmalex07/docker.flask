FROM python:3.6

LABEL language="python"
LABEL framework="flask"
LABEL usage="hello-world"

RUN apt-get update
RUN pip3 install flask

RUN mkdir /var/local/helloworld && chown www-data:www-data /var/local/helloworld

ADD wsgi.py /usr/local/bin/wsgi.py
RUN chmod +x /usr/local/bin/wsgi.py

COPY helloworld /usr/local/helloworld
RUN cd /usr/local/helloworld && python3 setup.py install

USER www-data
WORKDIR /var/local/helloworld

RUN mkdir ./logs
ADD logging.conf .

EXPOSE 5000

ENV FLASK_ENV="production" FLASK_DEBUG="false" 
ENV TLS_CERTIFICATE="" TLS_KEY=""

CMD ["/usr/local/bin/wsgi.py"]
