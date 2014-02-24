from blog import app
from flask import render_template
import json
import urllib2


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/stations')
def stations():
    divy_data = urllib2.urlopen('http://divvybikes.com/stations/json')
    divy_json = json.load(divy_data)
    divy = divy_json
    return render_template('stations.html', divy=divy)
