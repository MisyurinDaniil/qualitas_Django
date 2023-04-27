# Create your views here.

from .models import ProductItem, ProductCategory
from django.db.models import Q

from django.views.generic import ListView, DetailView
from appOrders.form import ReviewForm 

############ CBV test ############# 
class ProductsInCategoryList(ListView):
    """
        https://proproprogs.ru/django/klassy-predstavleniy-listview-detailview-createview
        model - сслылка на модель данных. 
        По умолчанию в контекст попадают все элементы модели ProductItem,
            эквивалента записи ProductItem.objects.all(), если не указвать def get_queryset() или queryset
        allow_empty = False - генерирует исключение 404 если список статей пуст 
        template_name = 'appProductItem/productitem_list.html' - Шаблон в который передается контекст,
            по умолчанию (если не указывать template_name) находится по пути <имя приложения>/<имя модели>_list.html 
        context - это данные которые передаются в шаблон. Представляет собой словарь.
            В словаре имеются два поля (значения), к этим полям можно обращатся напрямую из шаблона.
            Поля имеют следующие имена: 
                'view' - экзкмпляр нашего класа представления, в данном случае "ProductsInCategoryList"
                'object_list' или знчение из переменной context_object_name - это queryset объект полученный из модели данных,
                    путем выполнения запроса из self.get_queryset() или self.queryset. Queryset - это последовательность в которой
                    содержится результат выполнения запроса к БД, т.е. экземпляры класса model (ProductItem)
        Для передачи доплнительных данных в шаблон можно использовать следующие подходы, помимо get_queryset:
            1. Класс с методами, методы возвращают данные (например queryset). 
                затем этот класс подмешивается (mixin) к нашему представлению 
                и данные методы становятся доступными в template (django_movie_shots  - 17)
            2. Использовать get_context_data использование расписано ниже в классе
            3. Использовать simple tags (django_movie_shots  - 15)
            4. Определить метод в модели (django_movie_shots  - 10)
        paginate_by включает пагинацию 
    """
    model = ProductItem
    context_object_name = 'products'
    allow_empty = False
    # paginate_by = 1
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
    
    def get_context_data(self, *, object_list=None, **kwargs):
        """
            Метод для передачи дополнительных данных в контекст.
            Через переменную category в шаблоне доступен объект нужной категории.
        """
        context = super().get_context_data(**kwargs)
        context['category'] = ProductCategory.objects.get(product_category_slug = self.kwargs['productCategorySlug'])
        return context
    
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

    def get_context_data(self, *, object_list=None, **kwargs):
        """
            Метод для передачи дополнительных данных в контекст.
            Через переменную category в шаблоне доступен объект нужной категории.
        """
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context