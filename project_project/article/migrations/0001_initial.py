# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('article_title', models.CharField(max_length=250)),
                ('article_content', models.TextField()),
                ('article_author', models.CharField(max_length=50)),
                ('article_date', models.DateTimeField()),
                ('article_rate', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.EmailField(blank=True, max_length=254)),
                ('comment_date', models.DateTimeField(blank=True, default=0, null=True)),
                ('comment_content', models.TextField(blank=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
            ],
            options={
                'db_table': 'article_comments',
            },
        ),
    ]
