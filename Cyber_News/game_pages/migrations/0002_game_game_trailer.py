# Generated by Django 2.2.6 on 2019-11-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_trailer',
            field=models.URLField(default='NULL'),
        ),
    ]