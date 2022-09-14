from core.celery import app
from .service import send, send_contact_mail
from main.models import Contact
from django.core.mail import send_mail
from celery import shared_task


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    send_contact_mail()