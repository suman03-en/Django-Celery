from celery import shared_task
from django.core.mail import send_mail
from .utils import generate_report_card
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

@shared_task
def generate_report(data: dict):
    """takes the data and generate the report card"""
    filepath = generate_report_card(data)
    return f"PDF generated successfully: {filepath}"