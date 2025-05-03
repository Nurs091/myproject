
from django.core.mail import send_mail
from django.conf import settings
import random


def send_verification_code(email, code):
    subject = 'Registration confirmation code'
    message = f'Your verification code: {code}'
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, from_email, [email], fail_silently=False)


def generate_reset_code():
    return str(random.randint(100000, 999999))

def send_password_reset_code(email, code):
    subject = "Password Reset Code"
    message = f"Your password reset code is: {code}"
    send_mail(subject, message, 'your_email@gmail.com', [email])
