# Generated by Django 3.0.4 on 2020-04-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0017_auto_20200401_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmodule',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalseries',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
