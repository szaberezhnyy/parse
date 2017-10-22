# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory
from bs4 import BeautifulSoup
from collections import namedtuple
import sys
import requests

from .parser import parse_krysha

app = Flask(__name__, static_url_path='')


@app.route('/dist/<path:path>')
def send_css(path):
    return send_from_directory('templates/flat-ui-master/dist', path)


@app.route('/', methods=['GET'])
def hello_world():
    l = ['Name1', 'Name2', 'Name3']
    return render_template(
        'index.html',
        name='Sergey',
        list=l
    )

@app.route('/submit_form', methods=['POST'])
def receive_form():
    print (request.form)
    price_from = request.form['price_from']
    price_to = request.form['price_to']
    # square_from = request.form['square_from']
    # square_to = request.form['square_to']
    # floor_from = request.form['floor_from']
    # floor_to = request.form['floor_to']
    # year_from = request.form['year_from']
    # year_to = request.form['year_to']
    # result = parse_krysha(price_from, price_to)
    result = parse_krysha(price_from, price_to)
    return 'цена от '+price_from+' до '+price_to
