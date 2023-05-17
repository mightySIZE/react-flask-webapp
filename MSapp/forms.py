from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, DateField

class RegisterationForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    password1 = PasswordField('Password')
    password2 = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up') 