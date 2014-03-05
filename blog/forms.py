from wtforms import Form
from wtforms import TextField, SubmitField, ValidationError
from wtforms.validators import DataRequired

from blog.utils import get_user

def validate_login(form, field):

    user = get_user(form.username.data)

    if user is None:
        raise ValidationError('Invalid user')
    elif not user.check_password(form.password.data):
        raise ValidationError('bad password')

class Users_Form(Form):
    username = TextField('username', validators=[DataRequired(), validate_login])
    password = TextField('password', validators=[DataRequired()])
    submit = SubmitField()


