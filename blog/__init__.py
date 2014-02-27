from flask import Flask
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from admin import MyView
from blog.models import db, Users, Courses, Profile

app = Flask(__name__)

app.config.from_object('config')

db.init_app(app)


admin = Admin(app)
admin.add_view(MyView(name='Hello'))
admin.add_view(ModelView(Users, db.session))
admin.add_view(ModelView(Courses, db.session))
admin.add_view(ModelView(Profile, db.session))


from blog import views
