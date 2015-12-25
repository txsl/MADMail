from flask import Flask, render_template

from flask_mail import Mail


from config import SECRET_KEY, EMAIL

TEMPLATE_DIR = 'templates/'

app = Flask(__name__)


app.secret_key = SECRET_KEY

app.config.update(EMAIL)

mail = Mail(app)


@app.route("/")
def hello():
    return render_template('index.html')