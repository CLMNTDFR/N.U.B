# Generated by Django 5.0.6 on 2024-06-28 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_alter_band_year_formed'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
    ]
