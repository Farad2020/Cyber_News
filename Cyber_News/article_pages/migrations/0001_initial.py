from django.db import migrations, models


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
                ('game_developer', models.CharField(max_length=1000)),
                ('article_text', models.TextField(default='')),
                ('game_publisher', models.CharField(max_length=1000)),
                ('game_platforms', models.CharField(max_length=1000)),
                ('article_date', models.DateField(verbose_name='date published')),
                ('rating', models.FloatField(default=0.0)),
                ('article_img', models.ImageField(default='NULL', upload_to='article_img/')),
            ],
        ),
    ]
