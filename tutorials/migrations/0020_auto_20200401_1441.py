# Generated by Django 3.0.4 on 2020-04-01 18:41

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0019_auto_20200401_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltutorialsmetadata',
            name='series_desc',
            field=martor.models.MartorField(),
        ),
        migrations.AlterField(
            model_name='tutorialsmetadata',
            name='series_desc',
            field=martor.models.MartorField(),
        ),
    ]
