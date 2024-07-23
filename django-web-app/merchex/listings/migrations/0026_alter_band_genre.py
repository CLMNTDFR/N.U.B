# Generated by Django 5.0.6 on 2024-07-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0025_listing_image_alter_band_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(blank=True, choices=[('Metal', 'Metal'), ('Black Metal', 'Black Metal'), ('Death Metal', 'Death Metal'), ('Thrash Metal', 'Thrash Metal'), ('Power Metal', 'Power Metal'), ('Progressive Metal', 'Progressive Metal'), ('Symphonic Metal', 'Symphonic Metal'), ('Gothic Metal', 'Gothic Metal'), ('Folk Metal', 'Folk Metal'), ('Viking Metal', 'Viking Metal'), ('Sludge Metal', 'Sludge Metal'), ('Groove Metal', 'Groove Metal'), ('Industrial Metal', 'Industrial Metal'), ('Nu Metal', 'Nu Metal'), ('Djent', 'Djent'), ('Hardcore', 'Hardcore'), ('Beatdown Hardcore', 'Beatdown Hardcore'), ('Post-Hardcore', 'Post-Hardcore'), ('Melodic Hardcore', 'Melodic Hardcore'), ('Hardcore Punk', 'Hardcore Punk'), ('Crossover Thrash', 'Crossover Thrash'), ('Metalcore', 'Metalcore'), ('Mathcore', 'Mathcore'), ('Crust Punk', 'Crust Punk'), ('Extreme Metal', 'Extreme Metal'), ('Grindcore', 'Grindcore'), ('Brutal Death Metal', 'Brutal Death Metal'), ('Technical Death Metal', 'Technical Death Metal'), ('Deathgrind', 'Deathgrind'), ('Goregrind', 'Goregrind'), ('Pornogrind', 'Pornogrind'), ('Alternative and Fusion Genres', 'Alternative and Fusion Genres'), ('Alternative Metal', 'Alternative Metal'), ('Avant-Garde Metal', 'Avant-Garde Metal'), ('Funk Metal', 'Funk Metal'), ('Rap Metal', 'Rap Metal'), ('Jazz Metal', 'Jazz Metal'), ('Experimental Metal', 'Experimental Metal'), ('Doom and Stoner', 'Doom and Stoner'), ('Traditional Doom', 'Traditional Doom'), ('Funeral Doom', 'Funeral Doom'), ('Drone Doom', 'Drone Doom'), ('Psychedelic Doom', 'Psychedelic Doom'), ('Sludge Doom', 'Sludge Doom'), ('Desert Rock', 'Desert Rock'), ('Punk and Post-Punk', 'Punk and Post-Punk'), ('Anarcho-Punk', 'Anarcho-Punk'), ('Skate Punk', 'Skate Punk'), ('Pop Punk', 'Pop Punk'), ('Gothic Rock', 'Gothic Rock'), ('Deathrock', 'Deathrock'), ('Coldwave', 'Coldwave'), ('Noise and Experimental', 'Noise and Experimental'), ('Noise Rock', 'Noise Rock'), ('Noise Punk', 'Noise Punk'), ('Industrial Noise', 'Industrial Noise'), ('Noisecore', 'Noisecore'), ('Power Electronics', 'Power Electronics'), ('Experimental Rock', 'Experimental Rock'), ('Other Related Styles', 'Other Related Styles'), ('Grunge', 'Grunge'), ('Shoegaze', 'Shoegaze'), ('Post-Rock', 'Post-Rock'), ('Emo', 'Emo'), ('Screamo', 'Screamo'), ('Powerviolence', 'Powerviolence'), ('Alternative Rock', 'Alternative Rock')], max_length=30, null=True),
        ),
    ]