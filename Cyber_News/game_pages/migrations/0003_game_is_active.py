# Generated by Django 2.2.6 on 2019-12-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_pages', '0002_auto_20191207_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
    ]
