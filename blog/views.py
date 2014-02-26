from blog import app, db
from flask import render_template, request
from blog.forms import Users_Form
from blog.models import Users
import json
import urllib2
import hashlib


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/stations')
def stations():
    divy_data = urllib2.urlopen('http://divvybikes.com/stations/json')
    divy_json = json.load(divy_data)
    divy = divy_json
    return render_template('stations.html', divy=divy)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    Signup_Form = Users_Form()
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha1(request.form['password'])
        add_user = Users(username, password)
        db.session.add(add_user)
        db.session.commit()
        return render_template('/success.html')
    return render_template('signup.html', form=Signup_Form)
