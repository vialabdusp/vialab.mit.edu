# Generated by Django 3.0.4 on 2020-12-17 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0026_auto_20201217_1420'),
        ('classes', '0016_remove_classinstance_instructors'),
    ]

    operations = [
        migrations.AddField(
            model_name='classinstance',
            name='instructors',
            field=models.ManyToManyField(through='classes.InstructorOrder', to='people.Person'),
        ),
    ]
