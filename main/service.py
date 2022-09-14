from django.core.mail import send_mail
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from .templates.main import *
from main.models import Contact


def send(user_email):
    email_subject = 'Thank for your review'
    email_body = render_to_string('mail_p.html')

    email = EmailMultiAlternatives(
        email_subject, email_body,
        'our_test_celery@gmail.com', [user_email, ],
    )
    email.attach_alternative(email_body, "text/html")
    return email.send(fail_silently=False)


def send_contact_mail():
    for contact in Contact.objects.all():
        email_subject = 'Hello'
        email_body = render_to_string('mail_p.html')
        email = EmailMultiAlternatives(
            email_subject, email_body,
            'our_test_email@gmail.com',
            [contact.email]
        )
        email.attach_alternative(email_body, "text/html")
        return email.send(fail_silently=False)




