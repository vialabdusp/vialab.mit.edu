# Generated by Django 3.0.4 on 2020-04-01 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reading', '0008_auto_20200401_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readinglist',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='readinglist',
            old_name='modified',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='readingmetadata',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='readingmetadata',
            old_name='modified',
            new_name='modified_at',
        ),
        migrations.CreateModel(
            name='HistoricalReadingMetadata',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('desc', markdownx.models.MarkdownxField(blank=True, max_length=2000)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('modified_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical reading metadata',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalReadingList',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.CharField(blank=True, max_length=1000)),
                ('lib_type', models.CharField(choices=[('user', 'User Library'), ('group', 'Group Library')], default='group', max_length=5)),
                ('cite_style', models.CharField(choices=[('mla', 'Modern Language Association (MLA)'), ('chicago-author-date', 'Chicago (Author Date)'), ('taylor-and-francis-harvard-x', 'Harvard')], default='chicago-author-date', max_length=30)),
                ('collection_key', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('modified_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical reading list',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
