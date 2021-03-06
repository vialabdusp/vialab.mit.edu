# Generated by Django 3.0.4 on 2021-03-12 23:20

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210308_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmainmetadata',
            name='feature_vid',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mainmetadata',
            name='feature_vid',
            field=models.FileField(blank=True, default='', upload_to=main.models.vid_filename),
        ),
    ]
