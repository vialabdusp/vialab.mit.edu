# Generated by Django 3.0.4 on 2020-12-17 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0021_auto_20201216_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='abbr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='dept',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='short',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
