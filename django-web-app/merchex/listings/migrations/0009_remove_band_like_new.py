# Generated by Django 5.0.6 on 2024-06-28 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]
