# Generated by Django 2.2.6 on 2019-12-08 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_pages', '0011_comment_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
