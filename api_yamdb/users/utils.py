import string
from random import sample
from django.core.mail import send_mail
from api_yamdb.settings import YA_MAIL


LENGTH = 20


def generate_confirmation_code():
    letters_and_digits = string.ascii_letters + string.digits
    confirmation_code = ''.join(sample(letters_and_digits, LENGTH))
    return confirmation_code


def send_confirmation_code(email, confirmation_code):
    send_mail(
        subject='Код подтверждения',
        message=f'Ваш код подтверждения: {confirmation_code}',
        from_email=YA_MAIL,
        recipient_list=(email,),
        fail_silently=False,
    )
