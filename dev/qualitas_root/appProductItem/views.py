from django.shortcuts import render

# Create your views here.

from .models import ProductItem, ProductImg, ProductCategory, ProductGroup
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from django.views.generic.base import View

############ CBV test ############# 

class ProductsCategoryView(View):
    """
        Получаем список товаров категории по Slug категории
        Метод get() принемает GET запрос
    """
    def get(self, request, productCategorySlug):
        """
            request - информация от клиента
            products - полученный QuerySet на основании запроса к модели
            productCategorySlug - Slug из get запроса
            select_related - за один SQL запрос собирает данные из нескольких таблиц
            ProductItem.objects.select_related('product_category') - обращаемся к моделе ProductItem, 
                также забираем данные из модели ProductCategory через select_related('product_category')
            .filter - указываем условия выбора данных
        """
        products = (ProductItem.objects.select_related('product_category')
            .filter(Q(product_category__product_category_is_published = True)
                & Q(product_category__product_category_slug = productCategorySlug)
                & Q(product_is_published = True))
                )
        if len(products):
            """
                render() - функция, которая генерирует HTML-файлы при помощи шаблонов страниц 
                    и соответствующих данных.
                './category.html' - шаблон
                {'products' : products} - объект с данными. 'products' - переменаня через которую 
                    в шаблоне будут доступны данные
            """
            return render(request, './category.html', {'products' : products})
        else: 
            raise Http404()
    

class ProductView(View):
    def get(self, request, productItemSlug):
        try:
            product = (ProductItem
                .objects.select_related('product_category', 'product_color', 'product_material', 'product_fitting', 'product_make_time')
                .get(
                    Q(product_category__product_category_is_published = True) 
                    & Q(product_slug = productItemSlug) 
                    & Q(product_is_published = True)
                    )
                )
            return render(request, './product.html', {'product' : product})
        # Если ProductItem с определенным idProductItem не найден срабатывает исключение ObjectDoesNotExist,
        # обрабатываем его и вызываем исключение Http404
        except ObjectDoesNotExist:
            raise Http404()
