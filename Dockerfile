FROM debian:jessie

RUN apt-get update && apt-get install -y python python-pip python-flask python-flask-login

# Install our helloworld package
ADD helloworld /usr/local/helloworld
RUN cd /usr/local/helloworld && python setup.py install

ADD wsgi.py /usr/local/bin/wsgi.py

LABEL language="python"
LABEL framework="flask"
LABEL usage="hello-world"

ENV LISTEN_ADDRESS "0.0.0.0"

EXPOSE 5000

WORKDIR "/usr/local/"
ENTRYPOINT ["/usr/bin/python"]
CMD ["bin/wsgi.py"]
