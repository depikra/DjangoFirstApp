# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 00:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20161026_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 27, 0, 7, 7, 510621)),
        ),
    ]