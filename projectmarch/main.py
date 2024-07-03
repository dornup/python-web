from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from forms import RegisterForm, LoginForm
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user, login_required
import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
SECRET_KEY = os.urandom(32) #генерация уникальной последовательности из 32 байто


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)

#логин система
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

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
    name = db.Column(db.String(250), unique=False, nullable=False)
    password = db.Column(db.String(250), nullable=False) 

db.create_all()    

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route("/", methods=['GET', 'POST'])
def index():
    form = RegisterForm()
    if request.method == 'POST': # если пользователь что-то отправил
        if form.validate_on_submit(): #валидация (если форма сказала, что все окей)
            if User.query.filter_by(login=request.form.get('login')).first(): # если пользователь уже занят: почта занята
                return redirect(url_for('login'))
            else:  # иначе: хэшируем пароль, создать пользователя в бд, авторизация
                hashed_pass = generate_password_hash(
                    password = request.form.get('password'),
                    method = 'pbkdf2:sha256',
                    salt_length = 8)
                # определяем нового пользователя
                new_user = User(
                    login = request.form.get('login').lower() ,
                    name = request.form.get('name').capitalize() ,
                    password = hashed_pass
                )
                # заносим запись в бд
                db.session.add(new_user)
                db.session.commit()

                login_user(new_user)
                return redirect(url_for('home'))

    return render_template('index.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        user = User.query.filter_by(login=login).first()
        if not user:
            return redirect(url_for('index'))
        # не хватает проверки пароля
        else:  # когда логин есть
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('home'))
            else:
                print('НЕ')
    return render_template('login.html', form=form)

@app.route("/home")
@login_required
def home():
    return render_template('home.html')

app.run(debug=True)