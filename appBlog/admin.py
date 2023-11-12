from django.contrib import admin
# from django.db import models
# from django.forms import TextInput, Textarea
from django.utils.safestring import mark_safe
from .models import BlogArticle


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
    # Укажем сколько строк на одной странице
    list_per_page = 15
    # Дублируем кнопки сохранения изменений на верху окна
    save_on_top = True
    # Укажем максимальное количество полей при выводе всех
    list_max_show_all = 100
    # Автоматически заполняем поле product_slug информацией из поля product_name, переведенную в формат Slug
    prepopulated_fields = {'slug': ('name',)}

    def get_img(self, obj):
        '''Функция для отображения миниатюры картинки в админ панеле'''
        if obj.img_main_small:
            return mark_safe(f'<img src="{obj.img_main_small.url}" width="80px"')
        else:
            return 'нет картинки'
    # Строковое представление функции get_img
    get_img.short_description = 'Миниатюра 400х267'

    # formfield_overrides = {
    #     models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    # }

    def get_form(self, request, obj=None, **kwargs):
        form = super(CustomizeBlogArticle, self).get_form(request, obj, **kwargs)
        form.base_fields['text_aticle'].widget.attrs['style'] = 'width: 900px; height: 700px'
        return form


admin.site.register(BlogArticle, CustomizeBlogArticle)
