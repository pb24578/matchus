# Generated by Django 3.1.2 on 2020-10-17 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
