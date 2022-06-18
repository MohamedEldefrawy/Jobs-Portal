from django.core.mail import send_mail
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.utils import timezone
from notification.models import Notification

from .models import Job


@receiver(m2m_changed, sender=Job.tags.through)
def job_creation_signal_handle(sender, instance, action, **kwargs):
    if action == 'post_add':
        job_tags = instance.tags.all()
        subject = "New Job has been created"
        msg = f'Job name: {instance.name}\n description: {instance.description}\n'
        users = []
        user_emails = []

        for tag in job_tags:
            users.append(tag.user_set.all())
        for user_query in users:
            for user in user_query.all():
                notification = Notification(message=msg, creation_time=timezone.now(), status=False)
                notification.users = user
                notification.save()
                user_emails.append(user.email)

        send_mail(subject=subject, message=msg, from_email="Jobs@Jobs.com", recipient_list=user_emails)
