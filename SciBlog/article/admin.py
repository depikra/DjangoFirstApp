from django.contrib import admin
from .models import Article, Comments

# Register your models here.
class ArticleInLine(admin.StackedInline):
    model = Comments
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_content', 'article_author', 'article_date']
    inlines = [ArticleInLine]
    list_display = ('article_title', 'article_date')
    list_filter =  ['article_date', 'article_author']

admin.site.register(Article, ArticleAdmin)