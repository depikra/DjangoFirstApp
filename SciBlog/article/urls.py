from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^1/', views.basic_one),
    # url(r'^2/', views.template_two),
    url(r'^$', views.template_simple)
]