# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 01:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20161027_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_author',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 10, 27, 1, 18, 38, 896624)),
        ),
    ]
