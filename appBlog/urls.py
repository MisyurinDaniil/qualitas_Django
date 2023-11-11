from django.urls import path
from . import views


urlpatterns = [
    path('blog/<slug:blogPageSlug>', views.BlogDetail.as_view(), name='finalblogpage'),
    path('blog', views.BlogList.as_view(), name='blog'),
]
