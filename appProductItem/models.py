from django.db import models

# Create your models here.

from django.urls import reverse

# Create your models here.

# Формирование модели "Категория товара" (сумки, кошельки и тд)
class ProductCategory(models.Model):
    # product_category_name - имя поля таблицы с типом CharField
    # max_length - максимальное количество симоволо
    # verbose_name - имя поля отображаемого в админ панеле
    product_category_name = models.CharField(max_length=255, verbose_name='Название категории товара для меню')
    product_category_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    product_category_is_published = models.BooleanField(default=True, verbose_name='Разрешить публикацию категории')

    # Убрал поле т.к. для формирования заголовка использую 
    # конструкция типа {{prodCategory.product_category_h1}} | Мастерская кожаных изделий ручной работы "Qualitas" 
    # product_category_title= models.CharField(verbose_name='Заголовок страницы браузера (<title>)', max_length=80)
    product_category_description = models.TextField(verbose_name='Описание страницы SEO (description)', max_length=200)
    product_category_keywords = models.CharField(verbose_name='Ключевые слова SEO (keywordss)', max_length=255)
    product_category_h1 = models.CharField(verbose_name='Большой заголовок H1', max_length=255)
    product_category_h2 = models.CharField(verbose_name='Маленький заголовок H2', max_length=255)
    product_category_img_main = models.ImageField(upload_to='category_img/', verbose_name='Фото для меню категории 210х140')
    product_category_img_main_alt = models.CharField(verbose_name='Атрибут alt основного фото категории', max_length=80)
    product_category_img_main_title = models.CharField(verbose_name='Атрибут title основного фото категории', max_length=80)
    product_category_img_mobile = models.ImageField(upload_to='category_img/', verbose_name='Фото шапки для стр. категории - mobile 576х568')
    product_category_img_mobile_horizontal = models.ImageField(upload_to='category_img/', verbose_name='Фото шапки  для стр. категории - mobile 768х568')
    product_category_img_tablet = models.ImageField(upload_to='category_img/', verbose_name='Фото шапки для стр. категории - tablet 1200х550')
    product_category_img_desktop = models.ImageField(upload_to='category_img/', verbose_name='Фото шапки для стр. категории - desktop 1440х760')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.product_category_name
    # get_absolute_url - позволяет получить канонический URL обьекта, при условии что этот метод определён.
    # Генерируем динамическую ссылку для категории товара
    # На основнаии шаблона прописанного в url.py     path('category<slug:productCategorySlug>', getPage.category_page, name='category'),
    # будет формироваться ссылка. Вместо productCategorySlug подставится значение из БД product_category_slug
    # и получим category/product_category_slug
    def get_absolute_url(self):
        return reverse('category', kwargs={'productCategorySlug': self.product_category_slug})

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "7. Категории товаров"


class ProductGroup(models.Model):
    # product_group_name - имя поля таблицы с типом CharField
    # max_length - максимальное количество симоволо
    # verbose_name - имя поля отображаемого в админ панеле
    product_group_name = models.CharField(max_length=255, verbose_name='Группа товара')
    product_group_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    product_group_is_published = models.BooleanField(default=True, verbose_name='Разрешить публикацию группы на главной странице')
    product_group_short_name = models.CharField(max_length=255, default='sale', verbose_name='Короткое имя (sale, hot, new...)')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.product_group_name

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Группа товара"
        verbose_name_plural = "8. Группы товаров"

# Создаем класс (модел) для таблицы цвета
class ProductColor(models.Model):
    # color - имя поля таблицы с типом CharField
    # max_length - максимальное количество симоволо
    # verbose_name - имя поля отображаемого в админ панеле
    colorName = models.CharField(max_length=255, verbose_name='Цвет')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.colorName

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "3. Цвета"

# Создаем класс (модел) для таблицы Материалы
class ProductMaterial(models.Model):
    materialName = models.CharField(max_length=255, verbose_name='Материал')

    def __str__(self):
        return self.materialName

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "4. Материалы"

# Создаем класс (модел) для таблицы Фурнитура
class ProductFitting(models.Model):
    fittingName = models.CharField(max_length=255, verbose_name='Фурнитура')

    def __str__(self):
        return self.fittingName

    class Meta:
        verbose_name = "Фурнитура"
        verbose_name_plural = "5. Фурнитруа"  

# Создаем класс (модел) для таблицы Время изготовления
class ProductMakeTime(models.Model):
    make_time = models.CharField(max_length=255, verbose_name='Время изготовления')

    def __str__(self):
        return self.make_time

    class Meta:
        verbose_name = "Время изготовления"
        verbose_name_plural = "6. Время изготовления"  

# Создаем класс (модел) для таблицы Товар
class ProductItem(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='Наименование товара')
    product_is_published = models.BooleanField(default=True, verbose_name='Разрешить публикацию')
    product_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL (формирует автоматически из "Наименование товара")')
    
    # Убрал поле т.к. для формирования заголовка использую 
    # конструкция типа {{prodItem.product_name}} | Мастерская кожаных изделий ручной работы "Qualitas"
    # product_page_title= models.CharField(verbose_name='Заголовок страницы браузера (<title>)', max_length=80)
    product_page_description = models.TextField(verbose_name='Описание страницы SEO (description)', max_length=200)
    product_page_keywords = models.CharField(verbose_name='Ключевые слова SEO (keywordss)', max_length=255)
    
    product_category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, verbose_name='Категория')
    product_group = models.ForeignKey(ProductGroup, on_delete=models.PROTECT, verbose_name='Группа')
    product_price = models.CharField(max_length=255, verbose_name='Цена')
    product_old_price = models.CharField(max_length=255, default=None,  verbose_name='Старая цена', blank=True)
    product_color = models.ForeignKey(ProductColor, on_delete=models.PROTECT, verbose_name='Цвет')
    product_material = models.ForeignKey(ProductMaterial, on_delete=models.PROTECT, verbose_name='Материал')
    # Связываем таблицы через тип поля ForeignKey, вторым параметром указывается что делать при
    # удалении поля (on_delete=models.PROTECT - запрещает удалять поля при удалении родителя)
    # blank - для пустоты в админ панели django
    product_fitting = models.ForeignKey(ProductFitting, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Фурнитура')
    product_make_time = models.ForeignKey(ProductMakeTime, on_delete=models.PROTECT, verbose_name='Время изготовления')
    product_size = models.CharField(max_length=255, verbose_name='Размер')
    product_description = models.TextField(verbose_name='Описание')
    product_img_main = models.ImageField(upload_to='product_item_img/', verbose_name='Основное фото товара 360х240')
    product_img_main_alt = models.CharField(verbose_name='Атрибут alt основного фото товара', max_length=80)
    product_img_main_title = models.CharField(verbose_name='Атрибут title основного фото товара', max_length=80)
    product_time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    product_time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.product_name

    # Генерируем динамическую ссылку для товара
    def get_absolute_url(self):
        return reverse('product', kwargs={'productItemSlug': self.product_slug})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "1. Товары"

# Создаем класс (модел) для таблицы Картинки товара
class ProductImg(models.Model):
    # Связываем таблицы через тип поля ForeignKey
    # on_delete=models.CASCADE - при удалении родителя (товара) удалиться связанная с ним таблица (картинки)
    img_binding = models.ForeignKey(ProductItem, on_delete=models.CASCADE, verbose_name='Товар')

    product_img = models.ImageField(upload_to='product_item_img/', verbose_name='Средное фото 570х380')
    product_img_alt = models.CharField(verbose_name='Атрибут alt среднего фото', max_length=80)
    product_img_title = models.CharField(verbose_name='Атрибут title среднего фото', max_length=80)

    product_img_big = models.ImageField(upload_to='product_item_img/', verbose_name='Большое фото 1280х853')
    product_img_big_alt = models.CharField(verbose_name='Атрибут alt большого фото', max_length=80)
    product_img_big_title = models.CharField(verbose_name='Атрибут title большого фото', max_length=80)

    def __str__(self):
        return self.product_img_alt

    class Meta:
        verbose_name = "Картинки для конечной страницы товара"
        verbose_name_plural = "2. Картинки для конечной страницы товара"

class Review(models.Model):
    userName = models.CharField(max_length=255, verbose_name='Имя пользователся')
    text = models.TextField(max_length=2000, verbose_name='Текст отзыва')
    stars = models.SmallIntegerField(default=0, verbose_name='Количество звезд рейтинга')
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return f"{self.name} - {self.product}"
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
