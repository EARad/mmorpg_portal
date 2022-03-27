from celery import shared_task

from django.core.mail import EmailMultiAlternatives


@shared_task
def send_mail(mail_to, mail_subject, mail_txt_content, mail_html_content):
    msg = EmailMultiAlternatives(
        subject=mail_subject,
        body=mail_txt_content,
        to=mail_to,
    )
    msg.attach_alternative(mail_html_content, "text/html")

    msg.send()
