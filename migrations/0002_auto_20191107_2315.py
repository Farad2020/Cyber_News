# Generated by Django 2.2.6 on 2019-11-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cyber_News_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamepage',
            name='game_rd',
            field=models.DateField(verbose_name='date published'),
        ),
    ]