# Generated by Django 3.0.4 on 2021-02-11 21:05

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0030_auto_20200408_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsoftware',
            name='desc',
            field=martor.models.MartorField(max_length=400),
        ),
        migrations.AlterField(
            model_name='software',
            name='desc',
            field=martor.models.MartorField(max_length=400),
        ),
    ]
