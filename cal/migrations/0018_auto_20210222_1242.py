# Generated by Django 3.0.4 on 2021-02-22 17:42

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0017_auto_20210222_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='title', unique=True),
        ),
    ]
