import logging
import urllib
import json

from flask import Flask
from flask import request, session, current_app
from flask import url_for, make_response, redirect, abort
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    current_app.logger.info("hello: params=%s headers=%s environ=%s", \
        dict(request.values), dict(request.headers), dict(request.environ));
    response = make_response("Hello Flask!", 200);
    response.headers['x-foo'] = 'Bar';
    return response;

@app.route("/get")
def get():
    r = {
        "params": dict(request.values),
        "headers": dict(request.headers),
    };
    response = make_response(r, 200);
    response.headers['content-type'] = 'application/json; charset=utf-8';
    return response;

@app.route("/fail")
def fail():
    h = request.headers;
    p = request.values;
    raise Exception("ooops");
