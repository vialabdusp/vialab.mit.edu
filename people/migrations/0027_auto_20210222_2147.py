# Generated by Django 3.0.4 on 2021-02-23 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0026_auto_20201217_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
        migrations.DeleteModel(
            name='HistoricalPerson',
        ),
    ]
