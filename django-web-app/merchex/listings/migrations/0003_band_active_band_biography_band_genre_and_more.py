# Generated by Django 5.0.6 on 2024-06-28 12:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='band',
            name='biography',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='genre',
            field=models.CharField(blank=True, choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock'), ('POP', 'Pop'), ('ROCK', 'Rock'), ('JAZZ', 'Jazz'), ('BLUES', 'Blues'), ('ELECTRONIC', 'Electronic'), ('FOLK', 'Folk'), ('COUNTRY', 'Country'), ('REGGAE', 'Reggae'), ('CLASSICAL', 'Classical'), ('METAL', 'Metal'), ('PUNK', 'Punk'), ('R_AND_B', 'R&B'), ('SOUL', 'Soul'), ('FUNK', 'Funk'), ('DISCO', 'Disco'), ('LATIN', 'Latin'), ('WORLD', 'World')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='official_homepage',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(default=1900, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2024)]),
            preserve_default=False,
        ),
    ]