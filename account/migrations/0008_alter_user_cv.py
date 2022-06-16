# Generated by Django 4.0.5 on 2022-06-16 14:48

import account.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_user_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='static/developers_cv', validators=[account.validators.Validators.validate_file_extension]),
        ),
    ]
