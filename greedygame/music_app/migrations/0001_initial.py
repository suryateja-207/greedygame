# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicGenre',
            fields=[
                ('genre_name', models.CharField(max_length=40, unique=True)),
                ('genre_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MusicTrack',
            fields=[
                ('title', models.CharField(max_length=40, unique=True)),
                ('rating', models.IntegerField()),
                ('track_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MusicTrackGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.MusicGenre')),
                ('track_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.MusicTrack')),
            ],
        ),
    ]
