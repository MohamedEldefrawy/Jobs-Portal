from django.core.validators import FileExtensionValidator
from django.db import models


class CV(models.Model):
    cv = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, default='',
                          validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    users = models.ForeignKey(
        'account.User', on_delete=models.CASCADE, null=True)
