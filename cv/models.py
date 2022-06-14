from django.core.validators import FileExtensionValidator
from django.db import models


class Cv(models.Model):
    file_path = models.CharField(max_length=500)
    cv = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, default='',
                          validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    user = models.ForeignKey(
        'account.User', on_delete=models.CASCADE, null=True)
