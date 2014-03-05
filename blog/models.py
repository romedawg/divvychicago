from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(120))
    profile = db.relationship('Profile', backref="users", uselist=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %s>' % (self.username)

    def __str__(self):
        return self.username


class Profile(db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.userid'))


    def __repr__(self):
        return "<Profile(email='%s')>" % self.email

    
class Courses(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    coursecode = db.Column(db.String(5))
    couretitle = db.Column(db.String(120))
    classnum = db.Column(db.String(120))
    status = db.Column(db.String(120))
    duration = db.Column(db.Integer)
    category = db.Column(db.Text)
    subcategory = db.Column(db.Text)

    def __repr_(self):
        return "<course %s>" % self.coursecode
