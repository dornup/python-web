from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import RegisterForm

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    # form = RegisterForm()
    return render_template('header.html', )

# @app.route("/about")
# def about_f():
#     return render_template('bimbam.html')

app.run(debug=True)