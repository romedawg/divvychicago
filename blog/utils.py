import os
from functools import partial

from blog import app, login_manager
from blog.models import Users

@login_manager.user_loader
def get_user(username):
    return Users.query.filter_by(username=username.first())
