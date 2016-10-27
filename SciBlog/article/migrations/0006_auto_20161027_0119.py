# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 01:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20161027_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_author',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 10, 27, 1, 19, 56, 925117)),
        ),
    ]