from blog import app, db
from flask import render_template, request, session, redirect, url_for
from blog.forms import Users_Form
from blog.models import Users
import json
import urllib2
import hashlib
from sqlalchemy.sql import exists


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/stations')
def stations():
    divy_data = urllib2.urlopen('http://divvybikes.com/stations/json')
    divy_json = json.load(divy_data)
    divy = divy_json
    return render_template('stations.html', divy=divy)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = Users_Form()
    flash = []
    if request.method == 'POST':
        if db.session.query(exists().where(Users.username==request.form['username'])).scalar():
            flash.append('username already exists')
            return render_template('signup.html', form=form, flash=flash)
        else:
            username = request.form['username']
            password = hashlib.sha1(request.form['password'])
            add_user = Users(username, password)
            db.session.add(add_user)
            db.session.commit()
            return redirect(url_for('home'))
    flash.append('enter a username/password')
    return render_template('signup.html', form=form, flash=flash)

    if request.method == 'GET':
        return render_template('signup.html', form=form)

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    flash = []
    if 'username' in session:
        return render_template('profile.html')
    flash.append('please login')
    return redirect(url_for('signup', flash=flash))
