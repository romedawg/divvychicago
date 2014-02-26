from wtforms import Form
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired

class Users_Form(Form):
    username = TextField('username', validators=[DataRequired()])
    password = TextField('password', validators=[DataRequired()])
    submit = SubmitField()

