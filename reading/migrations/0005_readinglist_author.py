# Generated by Django 3.0.4 on 2020-03-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('reading', '0004_auto_20200322_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='readinglist',
            name='author',
            field=models.ManyToManyField(to='people.Person'),
        ),
    ]
