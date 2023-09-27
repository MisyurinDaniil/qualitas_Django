from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('contacts', views.contacts_page, name='contacts'),
    path('delivery', views.delivery_page, name='delivery'),
    path('payment', views.payment_page, name='payment'),
    path('personalization/tisnenie', views.tisnenie_page, name='tisnenie'),
    path('personalization/lazernaya-gravirovka', views.lazernaya_gravirovka_page, name='lazernaya_gravirovka'),
    path('personalization/kozha-nit-furnitura', views.kozha_nit_furnitura, name='kozha_nit_furnitura'),
    # path('aboutus', getPage.aboutus_page, name='aboutus'),
    # path('help', getPage.help_page, name='help'),
]
