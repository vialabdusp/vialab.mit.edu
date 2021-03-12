# Generated by Django 3.0.4 on 2020-03-30 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_person_zotero'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('D', 'Director'), ('C', 'Affiliate'), ('R', 'Research Assistant'), ('F', 'Faculty Steering Committee'), ('A', 'Alumni Board')], default='', max_length=1),
            preserve_default=False,
        ),
    ]
