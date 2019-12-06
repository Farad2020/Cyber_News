# Generated by Django 2.2.6 on 2019-12-06 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game_pages', '0010_auto_20191205_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_score',
        ),
        migrations.AlterField(
            model_name='game',
            name='game_genre',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Action', 'Action'), ('FPS', 'FPS'), ('Strategy', 'Strategy'), ('Shooter', 'Shooter'), ('Platformer', 'Platformer'), ('Fighting', 'Fighting'), ("Beat 'em up", "Beat 'em up"), ('Stealth', 'Stealth'), ('Survival', 'Survival'), ('Battle Royale', 'Battle Royale'), ('Rhythm games', 'Rhythm games'), ('Survival horror', 'Survival horror'), ('Metroidvania', 'Metroidvania'), ('Visual novels', 'Visual novels'), ('Interactive movie', 'Interactive movie'), ('Action RPG', 'Action RPG'), ('RPG', 'RPG'), ('JRPG', 'JRPG'), ('MMORPG', 'MMORPG'), ('Quest', 'Quest'), ('Roguelikes', 'Roguelikes'), ('Simulator', 'Simulator'), ('Strategy', 'Strategy'), ('MOBA', 'MOBA'), ('RTS', 'RTS'), ('Tower defense', 'Tower defense'), ('TBS', 'TBS'), ('Sports', 'Sports'), ('Racing', 'Racing'), ('MMO', 'MMO'), ('Soulslike', 'Soulslike'), ('Sandbox', 'Sandbox'), ('Adventure', 'Adventure'), ('Hack and slash', 'Hack and slash')], default=None, max_length=315),
        ),
        migrations.CreateModel(
            name='RatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0.0)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_pages.Game')),
                ('rater_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]