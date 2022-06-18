from account.models import User
from django.db import models


class Notification(models.Model):
    message = models.CharField(max_length=500)
    creation_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=5, default="False")
    users = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.message
