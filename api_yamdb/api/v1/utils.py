from django.core.mail import send_mail

from api_yamdb.settings import YA_MAIL


def send_confirmation_code(email, confirmation_code):
    send_mail(
        subject='Код подтверждения',
        message=f'Ваш код подтверждения: {confirmation_code}',
        from_email=YA_MAIL,
        recipient_list=(email,),
        fail_silently=False,
    )
