# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template
from lxml.etree import fromstring
import requests
import xmltodict

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.template')

@app.route('/weather/json/<path:location>')
def get_yr(location):
    #url = 'http://www.yr.no/sted/Norge/Akershus/B%C3%A6rum/Halden_brygge/varsel_time_for_time.xml'
    location = location.encode('utf-8').replace('æ', '%C3%A6')
    url = 'http://www.yr.no/sted/%s/varsel_time_for_time.xml' % (location)
    response = requests.get(url)
    content = response.content
    data = content
    data = xmltodict.parse(data)
    return jsonify(data)

@app.route('/weather/longterm/json/<path:location>')
def get_longterm_yr(location):
    #url = 'http://www.yr.no/sted/Norge/Akershus/B%C3%A6rum/Halden_brygge/varsel_time_for_time.xml'
    location = location.encode('utf-8').replace('æ', '%C3%A6')
    url = 'http://www.yr.no/sted/%s/forecast.xml' % (location)
    response = requests.get(url)
    content = response.content
    data = content
    data = xmltodict.parse(data)
    return jsonify(data)

application = app.wsgi_app

if __name__ == '__main__':
    app.run()
