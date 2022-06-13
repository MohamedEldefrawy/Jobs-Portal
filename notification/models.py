from django.db import models


class Notification(models.Model):
    message = models.CharField(max_length=50)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
