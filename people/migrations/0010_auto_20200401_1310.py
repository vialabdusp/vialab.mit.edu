# Generated by Django 3.0.4 on 2020-04-01 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_eventmetadata'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventMetadata',
            new_name='PeopleMetadata',
        ),
    ]
