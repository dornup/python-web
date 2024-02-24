from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
    login = StringField(label='Логин', validators=[
        DataRequired('Обязательно!!!'), 
        ])
    password = PasswordField(label='Пароль',validators=[
       DataRequired('Обязательно!!!'), 
       Length(min=8, max=16, message='Длина') 
    ])
    submit = SubmitField(label='Зарегистрироваться')