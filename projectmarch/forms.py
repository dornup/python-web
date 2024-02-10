from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RegisterForm(FlaskForm):
    email = StringField(label='Почта')
    submit = SubmitField(label='Зарегистрироваться')