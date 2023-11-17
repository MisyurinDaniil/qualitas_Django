from django.contrib import admin
# from django.db import models
# from django.forms import TextInput, Textarea
from django.utils.safestring import mark_safe
from .models import BlogArticle, BlogImage


class ShowImagesInBlogArticle(admin.StackedInline):
    # Указываем обязательный атрибут - модель к которой относится данный класс
    model = BlogImage
    # Указжем поля отображаемые на конечной странице
    fields = ('img_medium', 'img_big')
    # Укажем поля только для чтения, чтобы django не вывалилвался в ошибку
    readonly_fields = ('get_product_img_medium', 'get_product_img_big')

    def get_product_img_medium(self, obj):
        ''' Функция для отображения миниатюры картинки в админ панеле '''
        if obj.img_medium:
            return mark_safe(f'<img src="{obj.img_medium.url}" width="80px"')
        else:
            return 'нет картинки'

    def get_product_img_big(self, obj):
        ''' Функция для отображения миниатюры картинки в админ панеле '''
        if obj.img_big:
            return mark_safe(f'<img src="{obj.img_big.url}" width="80px"')
        else:
            return 'нет картинки'

    # Строковое представление функции get_img
    get_product_img_medium.short_description = 'Миниатюра 570х380'
    get_product_img_big.short_description = 'Миниатюра 1280х853'

    # Задаим одно поле ввода для модели ProductImg = 1, если указать 0 - необходимо нажимать зеленый плюс
    # для отображения полей ввода новых значений.
    extra = 0


class CustomizeBlogArticle(admin.ModelAdmin):
    # Кортеж с именами полей, который хотим отобразит в админ панеле на этапе просмотра всего перечня экземпляров
    list_display = ('id', 'name', 'get_img', 'is_published')
    # Отмечаем поля по нажатию на которые можно перейти на страницу экземпляра
    list_display_links = ('id', 'name', 'get_img')
    # Укажим поля по которым разрешена фильтрация товаров на этапе просмотра всего перечная
    # товаров
    list_filter = ('is_published',)
    # Определяем поля, которые можно отредактировать, не переходя на отдельный экземпляр
    list_editable = ('is_published', )
    # Укажим поля по которым разрешен поиск на этапе просмотра всего перечная товаров
    search_fields = ('name',)
    # Дублируем кнопки сохранения изменений на верху окна
    save_on_top = True
    # Автоматически заполняем поле product_slug информацией из поля product_name, переведенную в формат Slug
    prepopulated_fields = {'slug': ('name',)}
    # Передадим класс ProductImages для отображения полей добавления картинок на странице добавления товара
    # По умолчанию одается 3 поля сторонней модели
    inlines = [ShowImagesInBlogArticle, ]

    def get_img(self, obj):
        '''Функция для отображения миниатюры картинки в админ панеле'''
        if obj.img_main_small:
            return mark_safe(f'<img src="{obj.img_main_small.url}" width="80px"')
        else:
            return 'нет картинки'
    # Строковое представление функции get_img
    get_img.short_description = 'Миниатюра 400х267'

    def get_form(self, request, obj=None, **kwargs):
        form = super(CustomizeBlogArticle, self).get_form(request, obj, **kwargs)
        form.base_fields['text_aticle'].widget.attrs['style'] = 'width: 900px; height: 700px'
        return form


admin.site.register(BlogArticle, CustomizeBlogArticle)
