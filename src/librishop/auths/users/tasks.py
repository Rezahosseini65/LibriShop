from django.core.mail import send_mail

from celery import shared_task


@shared_task()
def send_password_change_email():
    # subject = "Password Change"
    # message = "Your password has been successfully changed."
    # send_mail(
    #      subject,
    #      message,
    #      'hosseini.jaamejam@gmail.com',
    #      [user_email],
    #      fail_silently=False
    #  )
    print("change password")
