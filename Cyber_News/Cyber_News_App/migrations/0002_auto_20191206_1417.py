# Generated by Django 2.2.6 on 2019-12-06 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cyber_News_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='article',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='author_id',
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='thread_author',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
