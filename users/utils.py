from django.core.mail import send_mail

def send_welcome_email(to_email):
    subject = 'Welcome to My Site'
    message = 'Thank you for registering with us. We are happy to have you as a user.'
    from_email = 'c2016830@my.shu.ac.uk'
    recipient_list = [to_email]

    send_mail(subject, message, from_email, recipient_list)
