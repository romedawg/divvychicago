from blog import app, db, login_manager
from flask import render_template, request, session, redirect, url_for, flash
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
    if request.method == 'POST':
        if db.session.query(exists().where(Users.username==request.form['username'])).scalar():
            return render_template('signup.html', form=form, flash=flash)
        else:
            username = request.form['username']
            password = hashlib.sha1(request.form['password'])
            add_user = Users(username, password)
            db.session.add(add_user)
            db.session.commit()
            session['username'] = username
            return redirect(url_for('profile'))
    return render_template('signup.html', form=form, flash=flash)

    if request.method == 'GET':
        return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Users_Form()
    if form.validate_on_submit():
        login_user(user)
        flash('logged in succesfully')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    flash = []
    form = Users_Form()
    if 'username' in session:
        return render_template('profile.html')
    flash.append('please login')
    return render_template('signup.html', flash=flash, form=form)

