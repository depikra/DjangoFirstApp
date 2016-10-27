# from django.shortcuts import render
# from django.http.response import HttpResponse
# from django.template.loader import get_template
# from django.template import Context
from django.shortcuts import render_to_response
from .models import Article, Comments
#<--SLOWLY WAY-->
# def basic_one(request):
#     view = "basic_one"
#     html = "<html><body>This is %s view</body></html>" %view
#     return HttpResponse(html)
#
# def template_two(request):
#     view = "template_two"
#     t = get_template('index.html')
#     u = {
#         'name': view
#     }
#     html = t.render(Context(u))
#     return HttpResponse(html)

#<--MOST FAST WAY-->

def template_simple(request):
    username = request.user
    return render_to_response('index.html', {
        'username': username,
        'articles': Article.objects.all(),
        'comment': Comments.comment_content
        #'article_title': Article.article_title,

    }
                              )

