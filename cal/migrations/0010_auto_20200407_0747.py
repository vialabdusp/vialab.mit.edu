# Generated by Django 3.0.4 on 2020-04-07 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0009_auto_20200407_0746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='historicalevent',
            old_name='name',
            new_name='title',
        ),
    ]
