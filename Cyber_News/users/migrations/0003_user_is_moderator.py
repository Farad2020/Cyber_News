# Generated by Django 2.2.6 on 2019-11-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_userimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_moderator',
            field=models.BooleanField(default=False, verbose_name='Moderator'),
        ),
    ]