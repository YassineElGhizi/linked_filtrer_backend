# Generated by Django 4.2.16 on 2024-09-18 15:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('linkedin', '0002_company_size_jobpost_work_mode_search_work_mode'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tracking',
            unique_together={('user', 'job_post')},
        ),
    ]
