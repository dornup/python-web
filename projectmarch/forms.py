from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

class RegisterForm(FlaskForm):
    email = StringField(label='Почта')
    password = PasswordField(label='Пароль')
    submit = SubmitField(label='Зарегистрироваться')