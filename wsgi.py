#!/usr/bin/env python
import os
import logging

from helloworld.app import app

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO);
    app.run(host="0.0.0.0");

