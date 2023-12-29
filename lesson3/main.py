from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', gagarin=True, crime=5)

app.run(debug=True)