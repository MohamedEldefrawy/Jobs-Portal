# Generated by Django 4.0.5 on 2022-06-15 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='accepted_dev',
        ),
    ]
