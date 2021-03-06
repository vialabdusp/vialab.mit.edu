# Generated by Django 3.0.4 on 2020-12-16 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0020_auto_20201216_1324'),
        ('main', '0008_auto_20200401_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmainmetadata',
            name='institution',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='people.Institution'),
        ),
        migrations.AddField(
            model_name='mainmetadata',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.Institution'),
        ),
        migrations.AlterField(
            model_name='historicalmainmetadata',
            name='main_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalmainmetadata',
            name='short_desc',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mainmetadata',
            name='main_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mainmetadata',
            name='short_desc',
            field=models.CharField(max_length=200),
        ),
    ]
