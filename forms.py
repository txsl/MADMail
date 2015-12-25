from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, length

class LoginForm(Form):
    username = StringField(u'Username', validators=[DataRequired(), length(max=10)])
    password = PasswordField(u'Password', validators=[DataRequired(), length(max=30)])
