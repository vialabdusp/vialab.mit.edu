# Generated by Django 3.0.4 on 2020-04-07 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0016_auto_20200406_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalperson',
            name='terminal_degree',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='person',
            name='terminal_degree',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
