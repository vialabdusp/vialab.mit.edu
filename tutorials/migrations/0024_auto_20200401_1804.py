# Generated by Django 3.0.4 on 2020-04-01 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0023_auto_20200401_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltutorialsmetadata',
            name='episode_name',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='tutorialsmetadata',
            name='episode_name',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
