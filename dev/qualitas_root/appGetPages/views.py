from django.shortcuts import render

# from appProductItem.views import getProdItemsByCategory, getProdItemBySlug, getProdImagesByProdSlug, getProductsCategoryBySlug

# # Create your views here.

def home_page(request):
    return render(request, './index.html')

# def product_page(request, productItemSlug):
#     # Получаем товар по productItemSlug товара 
#     prodItem = getProdItemBySlug(productItemSlug)
#     # Получаем картинки товараов по ID товара 
#     prodImages = getProdImagesByProdSlug(productItemSlug)
#     # Отрисовываем полученные данные на странице
#     return render(request, './product.html', {
#         'prodItem' : prodItem,
#         'prodImages' : prodImages,
#     })

# def category_page(request, productCategorySlug):
#     # Получаем список товаров определенной категории по Slug категории
#     prodItemsByCategory = getProdItemsByCategory(productCategorySlug)
#     # Получаем категорию товара по Slug категории, для вывода загаловков и картинки хедера
#     prodCategory = getProductsCategoryBySlug(productCategorySlug)
#     # Отрисовываем полученные данные на странице 
#     return render(request, './category.html', {
#         'prodItemsByCategory' : prodItemsByCategory,
#         'prodCategory' : prodCategory,
#     })

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