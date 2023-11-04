from django.urls import path

from . import views


urlpatterns = [
    path('blog', views.blog_page, name='blog'),
    path('finalblogpage', views.finalblogpage_page, name='finalblogpage'),
]
