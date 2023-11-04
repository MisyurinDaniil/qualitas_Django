from django.shortcuts import render

# from appProductItem.views import getProdItemsByCategory, getProdItemBySlug, getProdImagesByProdSlug, getProductsCategoryBySlug

# # Create your views here.

def home_page(request):
    return render(request, './index.html')

def aboutus_page(request):
    return render(request, './aboutus.html')

def contacts_page(request):
    return render(request, './contacts.html')

def delivery_page(request):
    return render(request, './delivery.html')

def help_page(request):
    return render(request, './help.html')

def payment_page(request):
    return render(request, './payment.html')

def tisnenie_page(request):
    return render(request, './tisnenie.html')

def lazernaya_gravirovka_page(request):
    return render(request, './lazernaya_gravirovka.html')

def kozha_nit_furnitura(request):
    return render(request, './kozha_nit_furnitura.html')

def page_not_found(request, exception):
    return render(request, './404.html', status = 404)