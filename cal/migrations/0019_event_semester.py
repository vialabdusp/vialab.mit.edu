# Generated by Django 3.0.4 on 2021-02-23 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0018_auto_20210222_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cal.Semester'),
        ),
    ]
