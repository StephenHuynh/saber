from flask import render_template
from flask import current_app
from flask_mail import Message

from threading import Thread
from project.extensions import mail


# HELPERS
def send_async_email(app, msg):
   with app.app_context():
      mail.send(msg)


def send_email(subject, sender, bcc, recipients, html_body):
   app = current_app._get_current_object()
   msg = Message(subject, sender=sender, bcc=bcc, recipients=recipients)
   msg.html = html_body
   thr = Thread(target=send_async_email, args=[app, msg])
   thr.start()
   return thr


def send_confirmation_order_email(user_email):
   html = render_template(
      'email_request_order.html')

   send_email('Your Order have been sent!', [user_email], html)