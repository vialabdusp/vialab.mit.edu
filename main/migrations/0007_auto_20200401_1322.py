# Generated by Django 3.0.4 on 2020-04-01 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200401_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmainmetadata',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainmetadata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
