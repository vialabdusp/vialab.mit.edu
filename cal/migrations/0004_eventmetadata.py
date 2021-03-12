# Generated by Django 3.0.4 on 2020-03-31 21:43

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_auto_20200322_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('desc', markdownx.models.MarkdownxField(blank=True, max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
