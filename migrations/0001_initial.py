# Generated by Django 2.2.6 on 2019-11-07 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=1000)),
                ('article_text', models.TextField(default='')),
                ('article_date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.FloatField(default=0.0)),
                ('numberOfClicks', models.IntegerField(default=0)),
                ('isBlog', models.BooleanField(verbose_name=True)),
            ],
        ),
        migrations.CreateModel(
            name='GamePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=1000)),
                ('game_developer', models.CharField(max_length=1000)),
                ('game_publisher', models.CharField(max_length=1000)),
                ('game_rd', models.DateTimeField(verbose_name='date published')),
                ('game_rating', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('isEditor', models.BooleanField(verbose_name=True)),
                ('isActive', models.BooleanField(verbose_name=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_text', models.TextField()),
                ('thread_date', models.DateTimeField(auto_now_add=True)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cyber_News_App.GamePage')),
                ('thread_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cyber_News_App.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_text', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cyber_News_App.Article')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cyber_News_App.User')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cyber_News_App.User'),
        ),
        migrations.AddField(
            model_name='article',
            name='game_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cyber_News_App.GamePage'),
        ),
    ]