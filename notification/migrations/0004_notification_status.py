# Generated by Django 4.0.5 on 2022-06-16 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_notification_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
