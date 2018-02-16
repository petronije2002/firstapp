#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:39:23 2018

@author: Pera
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World! First APP!!!!@@@@@@'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
