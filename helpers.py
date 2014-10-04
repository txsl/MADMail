# -*- coding: utf-8 -*-

from threading import Thread
from flask_mail import Message
import time
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import EMAIL
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

class BatchMail(object):

    def __init__(self):
        self.to_send = []

    def queue_mail(self, subject, sender, to_who, text_body="", html_body=""):
        msg = Message(subject=subject, sender=sender, recipients=to_who)
        msg.body = text_body
        msg.html = html_body
        self.to_send.append(msg)

    def send_queue(self):
        with app.app_context():
            with mail.connect() as conn:
                for item in self.to_send:
                    conn.send(item)
                    time.sleep(0.001)  # to avoid overloading the other end


def send_via_smtplib(subject, sender, to_who, text_body="", html_body=""):
    # headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n" % (sender, ", ".join(to_who), subject)
    msg = MIMEMultipart('alternative')
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(to_who)

    part1 = MIMEText(text_body, 'plain')
    part2 = MIMEText(html_body, 'html')

    msg.attach(part1)
    msg.attach(part2)

    s = smtplib.SMTP(EMAIL['MAIL_SERVER'])
    if EMAIL['MAIL_USE_TLS']:
        s.starttls()
    if EMAIL['MAIL_PASSWORD']:
        s.login(EMAIL['MAIL_USERNAME'], EMAIL['MAIL_PASSWORD'])
    s.set_debuglevel(1)
    s.sendmail(sender, to_who, msg.as_string())
    s.quit()



import re

TAG_RE = re.compile(r'<[^>]+>')

def strip_tags(text):
    return TAG_RE.sub('', text)

# from HTMLParser import HTMLParser
#
# class MLStripper(HTMLParser):
#     def __init__(self):
#         self.reset()
#         self.fed = []
#     def handle_data(self, d):
#         self.fed.append(d)
#     def get_data(self):
#         return ''.join(self.fed)
#
# def strip_tags(html):
#     s = MLStripper()
#     s.feed(html)
#     return s.get_data()