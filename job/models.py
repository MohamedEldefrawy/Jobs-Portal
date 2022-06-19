from django.db import models
from tag.models import Tag


class Job(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(
        'account.User',
        on_delete=models.CASCADE,
        null=True,
        related_name='creator',
    )
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag)
    banner_img = models.ImageField(upload_to='account', null=True, blank=True)
    status = models.CharField(
        choices=[('open', 'open'), ('in_progress', 'in_progress'), ('finished', 'finished')], max_length=20,
        default='open')
    accepted_dev = models.ForeignKey(
        'account.User',
        on_delete=models.CASCADE,
        related_name='accepted_dev',
        null=True,
        blank=True,
    )
    user_marked_done = models.BooleanField(default=False)
    creator_marked_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + self.creation_time.__str__()
