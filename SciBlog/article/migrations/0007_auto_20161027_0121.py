# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20161027_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(blank=True, default=0, null=True),
        ),
    ]