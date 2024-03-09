from django.core.mail import send_mail
from django.http import HttpResponse

def send_email(request):
    subject = 'Hello'
    message = 'Hi, this is a test email.'
    from_email = 'your_email@example.com'
    recipient_list = ['recipient@example.com']

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('Email sent successfully!')
