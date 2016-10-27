from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Article (models.Model):
    class Meta:
        db_table = 'article'

    id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=250)
    article_content = models.TextField()
    article_author = models.CharField(max_length=50)
    article_date = models.DateTimeField()
    article_rate = models.IntegerField(default = 0)

class Comments(models.Model):
    class Meta:
        db_table = 'article_comments'

    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    comment_author = models.EmailField(blank=True)
    comment_date = models.DateTimeField(null = True, blank = True, default=0)
    comment_content = models.TextField(blank=True)
