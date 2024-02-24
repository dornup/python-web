from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms import RegisterForm
from flask_login import UserMixin
import os
from flask_sqlalchemy import SQLAlchemy
SECRET_KEY = os.urandom(32) #генерация уникальной последовательности из 32 байтов


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)


# подключение бд
db_path = os.path.join(os.path.dirname(__file__), "users.db") #  путь до файла с бд 
db_url = f'sqlite:///{db_path}'  # ссылка на подключение к бд
app.config['SQLALCHEMY_DATABASE_URI'] = db_url # подружили алхимию и sqlite
db = SQLAlchemy(app)
# SQLALCHEMY - прослойка между sql и python
# sqlite - наша файловая база данных

# ================modeli bd
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

db.create_all()    

@app.route("/", methods=['GET', 'POST'])
def index():
    form = RegisterForm()
    if request.method == 'POST': # если пользователь что-то отправил
        if form.validate_on_submit(): #валидация (если форма сказала, что все окей)
            if User.query.filter_by(login=request.form.get('login')).first(): # если пользователь уже занят: почта занята
                print('ЛОГИН ЕСТЬ')
            else:  # иначе: хэшируем пароль, создать пользователя в бд, авторизация
                # определяем нового пользователя
                new_user = User(
                    login = request.form.get('login').lower() ,
                    password = request.form.get('password')
                )
                # заносим запись в бд
                db.session.add(new_user)
                db.session.commit()
    return render_template('index.html', form=form)

# @app.route("/about")
# def about_f():
#     return render_template('bimbam.html')

app.run(debug=True)