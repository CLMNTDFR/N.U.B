# Generated by Django 5.0.6 on 2024-07-08 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_band_photos_listing_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='band',
            name='photos',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
