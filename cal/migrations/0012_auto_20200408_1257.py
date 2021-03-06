# Generated by Django 3.0.4 on 2020-04-08 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0030_auto_20200408_1257'),
        ('cal', '0011_auto_20200407_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tutorials.Module'),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cal.Venue'),
        ),
    ]
