FROM python:3.6

LABEL language="python"
LABEL framework="flask"
LABEL usage="hello-world"

RUN apt-get update
RUN pip3 install flask

ADD helloworld /usr/local/helloworld
RUN cd /usr/local/helloworld && python3 setup.py install

ADD wsgi.py /usr/local/bin/wsgi.py
RUN chmod +x /usr/local/bin/wsgi.py

RUN mkdir /var/local/helloworld /var/local/helloworld/logs
ADD logging.conf /var/local/helloworld

EXPOSE 5000

ENV FLASK_ENV="production" FLASK_DEBUG="false" 
ENV TLS_CERTIFICATE="" TLS_KEY=""

WORKDIR /var/local/helloworld
CMD ["/usr/local/bin/wsgi.py"]
