"""qualitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .settings import DEBUG
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from appOrders.views import makeorder
from appGetPages import views as getPage
from appProductItem import views as product

urlpatterns = [
    path('', getPage.home_page, name='home'),
    path('product/<slug:productItemSlug>', product.ProductView.as_view(), name='product'),
    path('category/<slug:productCategorySlug>', product.ProductsCategoryView.as_view(), name='category'),
    path('blog', getPage.blog_page, name='blog'),
    path('finalblogpage', getPage.finalblogpage_page, name='finalblogpage'),
    path('aboutus', getPage.aboutus_page, name='aboutus'),
    path('contacts', getPage.contacts_page, name='contacts'),
    path('delivery', getPage.delivery_page, name='delivery'),
    path('payment', getPage.payment_page, name='payment'),
    path('help', getPage.help_page, name='help'),
    path('makeorder/', makeorder, name='makeorder'),
    path('admin', admin.site.urls),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
]
# Если включен DEBUG, меняем путь до статических файлов загруженных через админ панель
# (путь до файлов в папке media с включенным режимом DEBUG)
if DEBUG: 
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = getPage.page_not_found
