# Generated by Django 3.0.4 on 2020-03-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_person_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='zotero',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
    ]
