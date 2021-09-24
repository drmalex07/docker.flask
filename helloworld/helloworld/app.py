import logging
import urllib
import json
import os
import sys

import traceback
from itertools import chain

from werkzeug.exceptions import BadRequest

from flask import Flask
from flask import request, session, current_app
from flask import url_for, make_response, redirect, abort
from flask import render_template

app = Flask(__name__)

#
# Routing
#

@app.route("/")
def hello():
    current_app.logger.info("/: Generating a hello-world response");
    current_app.logger.debug("/: params=%s headers=%s environ=%s", \
        dict(request.values), dict(request.headers), dict(request.environ));
    response = make_response("Hello Flask (from %(HOSTNAME)s)!" % (os.environ), 200);
    response.headers['x-foo'] = 'Bar';
    return response;

@app.route("/get")
def get():
    current_app.logger.info("/get: Echoing parameters and headers...")
    r = {
        "params": dict(request.values),
        "headers": dict(request.headers),
    };
    response = make_response(r, 200);
    response.headers['content-type'] = 'application/json; charset=utf-8';
    return response;

@app.route("/post", methods=['POST', 'PUT'])
def post():
    r = {
        "params": dict(request.values),
        "headers": dict(request.headers),
        "body": request.json if request.is_json else None
    };
    response = make_response(r, 200);
    response.headers['content-type'] = 'application/json; charset=utf-8';
    return response;

@app.route("/redirect")
def redirect_to_get():
    location = url_for("get");
    current_app.logger.info("Redirecting to %s", location)
    return redirect(location);

@app.route("/unauthorized")
def unauthorized():
    current_app.logger.info("Not authorized");
    abort(401)

@app.route("/fail")
def fail():
    h = request.headers;
    p = request.values;
    raise BadRequest("ooops");

#
# Exception handling
#

class LoggingContextFilter(logging.Filter):

    def filter(self, record):
        record.msgid = 'hello-flask'
        if not hasattr(record, 'structured_data'):
            record.structured_data = {'mdc': {}}
        mdc = record.structured_data.get('mdc') 
        if mdc is None:
            mdc = record.structured_data['mdc'] = {}
        mdc.update({
            'logger': record.name,
            'thread': record.threadName
        })
        return True;

app.logger.addFilter(LoggingContextFilter())

@app.errorhandler(BadRequest)
def handle_bad_request(ex):
    extra = {
        'structured_data': {
            'mdc': {
                'key1': 'value1', 
                'key2': 'value2',
                'exception-message': ex.description,
                'exception': _format_traceback(),
            }
        }
    }
    current_app.logger.error("Bad request for [%s %s]: %s", 
        request.method, request.full_path, ex.description,
        extra=extra)
    
    return ex # ex is a valid response object    

def _format_traceback():
    '''Format traceback as a string without newlines'''
    tb = traceback.format_exception(*sys.exc_info());
    return '|'.join(chain.from_iterable((s.splitlines() for s in tb[1:])))

