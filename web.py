from flask import Flask
from flask_mail import Mail

from config import SECRET_KEY, EMAIL

app = Flask(__name__)
# app.debug = True

app.secret_key = SECRET_KEY

app.config.update(EMAIL)
# for key, item in EMAIL.iteritems():
#     if item is not None:
#         setattr(app, key, item)

mail = Mail(app)
