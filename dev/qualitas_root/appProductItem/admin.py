from django.contrib import admin
from django.utils.safestring import mark_safe

#from .models import ProductItem, ProductCategory, ProductGroup, ProductColor, ProductMaterial, ProductFitting, ProductMakeTime, ProductImg

from .models import *

# Register your models here.
class ShowImagesInProduct(admin.StackedInline):
    # Указываем обязательный атрибут - модель к которой относится данный класс
    model = ProductImg
    # Указжем поля отображаемые на карточке слайда
    fields = ('product_img', 'get_product_img', 'product_img_alt', 'product_img_title', 'product_img_big', 
                'get_product_img_big', 'product_img_big_alt', 'product_img_big_title')
    # Укажем поля только для чтения, чтобы django не вывалилвался в ошибку
    readonly_fields = ('get_product_img', 'get_product_img_big')
    # Функция для отображения миниатюры картинки в админ панеле

    def get_product_img(self, obj):
        if obj.product_img:
            return mark_safe(f'<img src="{obj.product_img.url}" width="80px"')
        else:
            return 'нет картинки'
    def get_product_img_big(self, obj):
        if obj.product_img_big:
            return mark_safe(f'<img src="{obj.product_img_big.url}" width="80px"')
        else:
            return 'нет картинки'

    # Строковое представление функции get_img
    get_product_img.short_description = 'Миниатюра 570х380'
    get_product_img_big.short_description = 'Миниатюра 1280х853'

    # Задаим одно поле ввода для модели Comment = 1, если указать 0 - необходимо нажимать зеленый плюс
    # для отображения поля комментария
    extra = 0


class CustomizeProductItem(admin.ModelAdmin):
    # Кортеж с именами полей, который хотим отобразит в админ панеле на этапе просмотра всего перечня товаров
    list_display = ('id', 'product_name', 'get_img', 'product_is_published')
    # Отмечаем поля по нажатию на которые можно перейти на страницу товара
    list_display_links = ('id', 'product_name', 'get_img')
    # Определяем поля, которые можно отредактировать, не переходя на отдельный товар
    list_editable = ('product_is_published', )
    # Указжем поля отображаемые на карточке товара
    fields = ('product_name', 'product_is_published', 'product_slug', 'product_page_title', 'product_page_description', 
        'product_page_keywords', 'product_category', 'product_group', 'product_price', 'product_old_price',
        'product_color', 'product_material', 'product_fitting', 'product_make_time', 'product_size', 
        'product_description', 'product_img_main', 'get_img', 'product_img_main_alt', 'product_img_main_title', 
        'product_time_create', 'product_time_update')
    # Укажем поля только для чтения, чтобы django не вывалилвался в ошибку
    readonly_fields = ('get_img', 'product_time_create', 'product_time_update')
    # Укажем сколько строк на одной странице
    list_per_page = 10
    # Укажем максимальное количество полей при выводе всех
    list_max_show_all = 100
    # Передадим класс ProductImages для отображения полей добавления картинок на странице добавления товара
    # По умолчанию одается 3 поля сторонней модели
    inlines = [ShowImagesInProduct,]
    # Автоматически заполняем поле product_slug информацией из поля product_name, переведенную в формат Slug
    prepopulated_fields = {'product_slug': ('product_name',)}
    # Функция для отображения миниатюры картинки в админ панеле
    def get_img(self, obj):
        if obj.product_img_main:
            return mark_safe(f'<img src="{obj.product_img_main.url}" width="80px"')
        else:
            return 'нет картинки'
    # Строковое представление функции get_img
    get_img.short_description = 'Миниатюра 360х240'

# Настраиваем отображение в админ панеле
class CustomProductCategory(admin.ModelAdmin):
    # Кортеж с именами полей, который хотим отобразит в админ панеле на этапе просмотра всего перечня категорий
    list_display = ('product_category_name', 'get_img', 'product_category_is_published')
    # Отмечаем поля по нажатию на которые можно перейти на страницу слайда
    list_display_links = ('product_category_name',)
    # Определяем поля, которые можно отредактировать, не переходя на отдельный слайд
    list_editable = ('product_category_is_published', )
    # Укажем поля только для чтения, чтобы django не вывалилвался в ошибку
    readonly_fields = ('id', )
    # Автоматически заполняем поле product_category_slug информацией из поля product_category_name, переведенную в формат Slug
    prepopulated_fields = {'product_category_slug': ('product_category_name',)}
    # Функция для отображения миниатюры картинки в админ панеле
    def get_img(self, obj):
        if obj.product_category_img_main:
            return mark_safe(f'<img src="{obj.product_category_img_main.url}" width="80px"')
        else:
            return 'нет картинки'
    # Строковое представление функции get_img
    get_img.short_description = 'Миниатюра 208х139'

# Настраиваем отображение в админ панеле
class CustomizeProductGroup(admin.ModelAdmin):
    # Кортеж с именами полей, который хотим отобразит в админ панеле на этапе просмотра слайдов
    list_display = ('product_group_name', 'product_group_is_published')
    # Отмечаем поля по нажатию на которые можно перейти на страницу слайда
    list_display_links = ('product_group_name',)
    # Определяем поля, которые можно отредактировать, не переходя на отдельный слайд
    list_editable = ('product_group_is_published', )
    # Укажем поля только для чтения, чтобы django не вывалилвался в ошибку
    readonly_fields = ('id', )
    # Автоматически заполняем поле product_group_slug информацией из поля product_group_name, переведенную в формат Slug
    prepopulated_fields = {'product_group_slug': ('product_group_name',)}


# Добавляем нашу модель в админ панель

class CustomizeProductImg(admin.ModelAdmin):
    # Кортеж с именами полей, который хотим отобразит в админ панеле на этапе просмотра всего перечня картинок
    list_display = ('id', 'get_product_img')
    # Отмечаем поля по нажатию на которые можно перейти на страницу слайда
    list_display_links = ('id', 'get_product_img')
    # Указжем поля отображаемые на карточке слайда
    fields = ('img_binding', 'product_img', 'get_product_img', 'product_img_alt', 'product_img_title', 'product_img_big', 'get_product_img_big', 
        'product_img_big_alt', 'product_img_big_title')
    # Укажем поля только для чтения, чтобы django не вывалилвался в ошибку
    readonly_fields = ('get_product_img', 'get_product_img_big')
    # Функция для отображения миниатюры картинки в админ панеле
    def get_product_img(self, obj):
        if obj.product_img:
            return mark_safe(f'<img src="{obj.product_img.url}" width="80px"')
        else:
            return 'нет картинки'
    def get_product_img_big(self, obj):
        if obj.product_img_big:
            return mark_safe(f'<img src="{obj.product_img_big.url}" width="80px"')
        else:
            return 'нет картинки'
    # Строковое представление функции get_img
    get_product_img.short_description = 'Миниатюра'
    get_product_img_big.short_description = 'Миниатюра'

# Добавляем нашу модель в админ панель
admin.site.register(ProductItem, CustomizeProductItem)
admin.site.register(ProductCategory, CustomProductCategory)
admin.site.register(ProductGroup, CustomizeProductGroup)
admin.site.register(ProductColor)
admin.site.register(ProductMaterial)
admin.site.register(ProductFitting)
admin.site.register(ProductMakeTime)
admin.site.register(ProductImg, CustomizeProductImg)