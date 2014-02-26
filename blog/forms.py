from wtforms import Form
from wtforms import TextField, SubmitField

class Users(Form):
    username = TextField()
    password = TextField()
    submit = SubmitField()

