# Generated by Django 5.0.6 on 2024-07-05 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_photo',
        ),
    ]
