# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmaper', '0011_auto_20160108_0702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nmapscan',
            name='slug',
        ),
        migrations.AddField(
            model_name='nmapscan',
            name='uuid',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]