# Generated by Django 3.0.4 on 2020-12-17 19:20

import classes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0010_auto_20201217_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='classinstance',
            name='syllabus',
            field=models.FileField(blank=True, default='', upload_to=classes.models.syllabus_filename),
        ),
    ]
