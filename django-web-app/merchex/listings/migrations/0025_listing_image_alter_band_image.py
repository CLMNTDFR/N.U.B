# Generated by Django 5.0.6 on 2024-07-15 09:30

import listings.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0024_band_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='listings/', validators=[listings.models.validate_image_file_extension, listings.models.validate_image_file_size]),
        ),
        migrations.AlterField(
            model_name='band',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='bands/', validators=[listings.models.validate_image_file_extension, listings.models.validate_image_file_size]),
        ),
    ]