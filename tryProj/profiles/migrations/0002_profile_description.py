# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default='default description text'),
        ),
    ]
