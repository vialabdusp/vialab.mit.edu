# Generated by Django 3.0.4 on 2020-04-07 11:46

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0008_auto_20200407_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=martor.models.MartorField(),
        ),
        migrations.AlterField(
            model_name='historicalevent',
            name='desc',
            field=martor.models.MartorField(),
        ),
    ]
