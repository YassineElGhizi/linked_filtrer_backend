# Generated by Django 4.2.16 on 2024-09-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='size',
            field=models.CharField(blank=True, choices=[('small', 'small'), ('medium', 'medium'), ('big', 'big')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='work_mode',
            field=models.CharField(blank=True, choices=[('hybrid', 'hybrid'), ('onsite', 'onsite'), ('remote', 'remote')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='work_mode',
            field=models.CharField(blank=True, choices=[('hybrid', 'hybrid'), ('onsite', 'onsite'), ('remote', 'remote')], max_length=50, null=True),
        ),
    ]
