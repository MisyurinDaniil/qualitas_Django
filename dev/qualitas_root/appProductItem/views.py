# Create your views here.

from .models import ProductItem
from django.db.models import Q

from django.views.generic import ListView, DetailView

############ CBV test ############# 
class ProductsInCategoryList(ListView):
    """
        https://proproprogs.ru/django/klassy-predstavleniy-listview-detailview-createview
        model сслылка на модель данных. Получает в контекст все элементы модели ProductItem
            и эквивалента записи ProductItem.objects.all(), если не указвать def get_queryset() или queryset
        allow_empty = False - генерирует исключение 404 если список статей пуст 
        template_name = 'appProductItem/productitem_list.html' - Шаблон в который передается контекст и 
            возвращается пользователю, по умолчанию (если не указывать template_name) находится 
            по пути <имя приложения>/<имя модели>_list.html 
        context - это данные которые передаются в шаблон. Представляет собой словарь.
            В словаре имеются два поля (значения), к этим полям можно обращатся напрямую из шаблона.
            Поля имеют следующие имена: 
                'view' - экзкмпляр нашего класа представления, в данном случае "ProductsInCategoryList"
                'object_list' или знчение из переменной context_object_name - это queryset объект полученный из модели данных,
                    путем выполнения запроса из self.get_queryset() или self.queryset
        Для передачи доплнительных данных в шаблон можно использовать следующие подходы, помимо get_queryset:
            1. Класс с методами, методы возвращают данные (например queryset). 
                затем этот класс подмешивается (mixin) к нашему представлению 
                и данные методы становятся доступными в template (django_movie_shots  - 17)
            2. Использовать get_context_data использование расписано ниже в классе
            3. Использовать simple tags (django_movie_shots  - 15)
            4. Определить метод в модели (django_movie_shots  - 10)
        
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
        context - это данные которые передаются в шаблон. Представляет собой словарь.
            В словаре имеются два поля (значения), к этим полям можно обращатся напрямую из шаблона.
            Поля имеют следующие имена: 
                'view' - экзкмпляр нашего класа представления, в данном случае "ProductsInCategoryList"
                'object' или знчение из переменной context_object_name - это queryset объект полученный из модели данных,
                    путем выполнения запроса из self.get_queryset() или self.queryset
        При попытке просмотра какого-либо поста, возникает исключение «AttributeError». 
            В чем проблема? Смотрите, вот этот класс DetailView по умолчанию пытается выбрать из указанной модели ProductItem запись, 
            используя атрибут pk или slug. Но у нас формируется маршрут с параметром productItemSlug из-за этого и возникает такая ошибка.
            Используем переменную slug_url_kwarg = 'productItemSlug' для обозначения своей переменной slug или ее нужно изменить в url.conf
        slug_url_kwarg - имя перемонной содержащей slug из url.conf
        slug_field-  Имя поля в модели, которое содержит slug. По умолчанию slug_field - 'slug'.

    """
    model = ProductItem
    context_object_name = 'product'
    slug_url_kwarg = 'productItemSlug'
    slug_field = 'product_slug'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        print(context['object'].__dict__)
        for key, items in context['object'].__dict__.items():
            print(key, " : ", items, '\n')
        print ('@' * 80)
        print(list(context['object'].productimg_set.all()))
        print(list(context['object'].productimg_set.all())[0].__dict__)
        print(context['object'].productimg_set.all().first())
        print ('@' * 80)
        return self.render_to_response(context)

    def get_object(self):
        try:
            product = (ProductItem.objects.get(Q(product_category__product_category_is_published = True) 
                & Q(product_slug = self.kwargs['productItemSlug']) 
                & Q(product_is_published = True)))
            # product = (ProductItem.objects.select_related('product_category', 'product_color', 'product_material', 'product_fitting', 'product_make_time')
            #     .get(Q(product_category__product_category_is_published = True) 
            #     & Q(product_slug = self.kwargs['productItemSlug']) 
            #     & Q(product_is_published = True)))
            return product
        except(ProductItem.DoesNotExist):
            from django.http import Http404
            raise Http404()
