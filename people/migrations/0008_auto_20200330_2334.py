# Generated by Django 3.0.4 on 2020-03-30 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_person_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('D', 'Director'), ('A', 'Affiliate'), ('R', 'Research Assistant'), ('F', 'Faculty Steering Committee'), ('L', 'Alumni Board')], default='', max_length=1),
        ),
    ]
