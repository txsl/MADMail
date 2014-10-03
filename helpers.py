from threading import Thread
from flask_mail import Message
from web import mail, app

def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


@async
def send_async_email(msg):
    with app.app_context():
        # print app.MAIL_SERVER
        mail.send(msg)

def send_mail(subject, sender, to_who, text_body="", html_body=""):
    msg = Message(subject=subject, sender=sender, recipients=to_who)
    msg.body = text_body
    msg.html = html_body
    send_async_email(msg)


from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()