#!/bin/sh
set -x
set -e

# Configure and start WSGI server

num_workers="2"
server_port="5000"
gunicorn_ssl_options=
if [ -n "${TLS_CERTIFICATE}" ] && [ -n "${TLS_KEY}" ]; then
    gunicorn_ssl_options="--keyfile ${TLS_KEY} --certfile ${TLS_CERTIFICATE}"
    server_port="5443"
fi

exec gunicorn --log-config logging.conf --access-logfile - \
  --workers ${num_workers} \
  --bind "0.0.0.0:${server_port}" ${gunicorn_ssl_options} \
  helloworld.app:app
