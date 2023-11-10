from django.urls import path
from . import views


urlpatterns = [
    path('blog', views.blog_page, name='blog'),
    # path('blog/<slug:blogPageSlug>', views.finalblogpage_page, name='finalblogpage'),
    path('finalblogpage', views.finalblogpage_page, name='finalblogpage'),
]
