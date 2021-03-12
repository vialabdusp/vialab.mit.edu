# Generated by Django 3.0.4 on 2020-04-08 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0018_auto_20200407_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperson',
            name='pronouns',
            field=models.CharField(choices=[('M', 'He/him/his'), ('W', 'She/her/hers'), ('N', 'He/him/his or They/them/theirs'), ('H', 'She/her/hers or They/them/theirs'), ('T', 'They/them/theirs')], default='T', max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='django_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='person',
            name='pronouns',
            field=models.CharField(choices=[('M', 'He/him/his'), ('W', 'She/her/hers'), ('N', 'He/him/his or They/them/theirs'), ('H', 'She/her/hers or They/them/theirs'), ('T', 'They/them/theirs')], default='T', max_length=1),
        ),
    ]
