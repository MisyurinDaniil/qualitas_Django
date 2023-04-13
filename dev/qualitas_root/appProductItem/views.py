# Create your views here.

from .models import ProductItem
from django.db.models import Q

from django.views.generic import ListView, DetailView

############ CBV test ############# 
class ProductsInCategoryList(ListView):
    """
        https://proproprogs.ru/django/klassy-predstavleniy-listview-detailview-createview
        model сслылка на модель данных. Данная строка получает в контекст все элементы модели ProductItem
            и эквивалента записи ProductItem.objects.all()
        По умолчанию, данные из модели ProductItem, указанной в классе представлений, помещаются в коллекцию object_list,
            которая предается в шаблон template/appProductItem/productitem_list.html. Чтобы поменять имя коллекциия
            используем переменную context_object_name = 'products'
        Генерировать исключение 404 если список статей пуст allow_empty = False
        Шаблон в который передается контекст и возвращается пользователю находится по пути <имя приложения>/<имя модели>_list.html 
            или используется атрибут template_name = 'appProductItem/productitem_list.html'
    """
    model = ProductItem
    context_object_name = 'products'
    allow_empty = False
    # template_name = 'appProductItem/productitem_list.html'

    def get_queryset(self):
        """
            Для получения данных из модели для передачи в контекст используется переменная queryset = ProductItem.objects.all() или
            метод получения записей get_queryset()
        """
        return (ProductItem.objects.select_related('product_category')
            .filter(Q(product_category__product_category_is_published = True)
            & Q(product_category__product_category_slug = self.kwargs['productCategorySlug'])
            & Q(product_is_published = True)))
    
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     """
    #         Для передачи шаблону таких статичных данных, можно использовать специальный словарь extra_context 
    #         extra_context = {'title': 'Главная страница'}. этот словарь можно использовать именно 
    #         для статичных (не изменяемых) данных, такие как строки, числа. Если же мы собираемся передавать 
    #         динамические данные, вроде списков, то для этого уже нужно переопределять метод get_context_data базового класса.
    #     """
    #     from qualitas.settings import DEBUG
    #     context = super().get_context_data(**kwargs)
    #     context['debug'] = DEBUG
    #     return context
    
class ProductDetail(DetailView):
    """
        При попытке просмотра какого-либо поста, возникает исключение «AttributeError». 
            В чем проблема? Смотрите, вот этот класс DetailView по умолчанию пытается выбрать из указанной модели ProductItem запись, 
            используя атрибут pk или slug. Но у нас формируется маршрут с параметром productItemSlug из-за этого и возникает такая ошибка.
            Используем переменную slug_url_kwarg = 'productItemSlug' для обозначения своей переменной slug или ее нужно изменить в url.conf
        slug_field-  Имя поля в модели, которое содержит slug. По умолчанию slug_field - 'slug'.

    """
    model = ProductItem
    context_object_name = 'product'
    slug_url_kwarg = 'productItemSlug'
    slug_field = 'product_slug'

    def get_object(self):
        try:
            product = (ProductItem.objects.select_related('product_category', 'product_color', 'product_material', 'product_fitting', 'product_make_time')
                .get(Q(product_category__product_category_is_published = True) 
                & Q(product_slug = self.kwargs['productItemSlug']) 
                & Q(product_is_published = True)))
            return product
        except(ProductItem.DoesNotExist):
            from django.http import Http404
            raise Http404()
