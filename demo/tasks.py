from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email, message, subject):
    response = send_mail(
        subject,
        message,
        from_email="sf@gmail.com",
        recipient_list=[user_email],
        fail_silently=False
    )
    return response