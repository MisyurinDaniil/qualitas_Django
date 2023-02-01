from django.shortcuts import render

# Create your views here.

from .models import ProductItem, ProductImg, ProductCategory, ProductGroup
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

############ Group function #############    
# Получаем все группы товаров
def getProductsGroups():
    return ProductGroup.objects.filter(product_group_is_published = True)

############ Category function #############
   
# Получаем категорию товара по ее Slug, для вывода имени категории в заголовок (переделать, ШЛЯПА)
def getProductsCategoryBySlug(productCategorySlug):
    try:
        return ProductCategory.objects.get(product_category_slug=productCategorySlug)
        # Если ProductCategory с определенным product_category_slug не найден срабатывает исключение ObjectDoesNotExist,
        # обрабатываем его и вызываем исключение Http404
    except ObjectDoesNotExist:
        raise Http404()

############ ProductItem function #############

# Получаем список товаров по Slug категории
def getProdItemsByCategory(productCategorySlug):
    pruducts = (ProductItem.objects.select_related('product_category')
                .filter(Q(product_category__product_category_is_published = True)
                    & Q(product_is_published = True)
                    & Q(product_category__product_category_slug = productCategorySlug)
                    )
                )
    if len(pruducts):
        return pruducts
    else: 
        raise Http404()
    
# Получаем товар по его Slug
def getProdItemBySlug(productItemSlug):
    try:
        return (ProductItem
                .objects.select_related('product_category', 'product_color', 'product_material', 'product_fitting', 'product_make_time')
                .get(
                    Q(product_category__product_category_is_published = True) 
                    & Q(product_slug = productItemSlug) 
                    & Q(product_is_published = True)
                    )
                )
        # Если ProductItem с определенным idProductItem не найден срабатывает исключение ObjectDoesNotExist,
        # обрабатываем его и вызываем исключение Http404
    except ObjectDoesNotExist:
        raise Http404()

# Получаем картинки товара по его Slug
def getProdImagesByProdSlug(productItemSlug):
    return ProductImg.objects.filter(img_binding__product_slug=productItemSlug)

# Получаем все товары находящиеся в группах
def getProdItemsInGroups():
    return (ProductItem
            .objects.select_related('product_group', 'product_category')
            .filter(
                Q(product_group__product_group_is_published = True) 
                & Q(product_category__product_category_is_published = True)
                & Q(product_is_published = True)
                )
            )

