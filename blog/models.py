from blog import db

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(120))
    profile = db.relationship('Profile', uselist=False, backref="users")

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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __repr__(self):
        return "<Profile(email='%s')>" % self.email

    
