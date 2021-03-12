# Generated by Django 3.0.4 on 2020-03-26 16:45

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0006_auto_20200326_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='desc',
            field=markdownx.models.MarkdownxField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='desc',
            field=markdownx.models.MarkdownxField(blank=True, max_length=1000),
        ),
    ]
