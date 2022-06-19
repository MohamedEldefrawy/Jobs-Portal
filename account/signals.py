from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User


@receiver(post_save, sender=User)
def user_creation_signal_handler(sender, instance, **kwargs):
    if kwargs.get('created'):
        created_object = kwargs.get('instance')
        print(created_object)
        subject = "New account has been created"
        msg = f'user name: {instance.username}\n email: {instance.email}'
        sender = "Jobs@Jobs.com"
        receivers = ['admin@admin.com']
        send_mail(subject=subject, message=msg,
                  from_email=sender, recipient_list=receivers)
