from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms import RegisterForm
import os
SECRET_KEY = os.urandom(32) #генерация уникальной последовательности из 32 байтов


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    form = RegisterForm()
    if request.method == 'POST': # если пользователь что-то отправил
        if form.validate_on_submit(): #валидация (если форма сказала, что все окей)
                pass
        # если пользователь уже занят: почта занята
        # иначе: хэшируем пароль, создать пользователя в бд, авторизация
    return render_template('index.html', form=form)

# @app.route("/about")
# def about_f():
#     return render_template('bimbam.html')

app.run(debug=True)