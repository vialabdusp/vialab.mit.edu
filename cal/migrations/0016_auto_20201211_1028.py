# Generated by Django 3.0.4 on 2020-12-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0015_auto_20201211_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='semester',
            field=models.CharField(choices=[('S', 'Spring'), ('3', 'Spring (H3)'), ('4', 'Spring (H4)'), ('F', 'Fall'), ('1', 'Fall (H1)'), ('2', 'Fall (H2)'), ('I', 'IAP'), ('M', 'Summer')], default='T', max_length=1),
        ),
    ]
