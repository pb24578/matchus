# Generated by Django 3.1.2 on 2020-11-03 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matchus', '0006_auto_20201103_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photos',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='No Name', max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='profilePhoto',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
