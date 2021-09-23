import logging
import urllib
import json
import os

from flask import Flask
from flask import request, session, current_app
from flask import url_for, make_response, redirect, abort
from flask import render_template

app = Flask(__name__)

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
    raise Exception("ooops");



