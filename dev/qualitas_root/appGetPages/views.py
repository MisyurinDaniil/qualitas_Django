from django.shortcuts import render

# from appProductItem.views import getProdItemsByCategory, getProdItemBySlug, getProdImagesByProdSlug, getProductsCategoryBySlug

# # Create your views here.

def home_page(request):
    return render(request, './index.html')

def blog_page(request):
    return render(request, './blog.html')

def finalblogpage_page(request):
    return render(request, './finalblogpage.html')

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

def page_not_found(request, exception):
    return render(request, './404.html')