from django.shortcuts import render
from .models import BlogArticle
from django.views.generic import ListView


def blog_page(request):
    return render(request, './appBlog/blog.html')


def finalblogpage_page(request):
    return render(request, './appBlog/finalblogpage.html')


class BlogList(ListView):
    """
        https://proproprogs.ru/django/klassy-predstavleniy-listview-detailview-createview
        model - сслылка на модель данных.
        По умолчанию в контекст попадают все элементы модели BlogArticle,
            эквивалента записи BlogArticle.objects.all(), если не указвать def get_queryset() или queryset
        allow_empty = False - генерирует исключение 404 если список статей пуст 
        template_name = 'appProductItem/productitem_list.html' - Шаблон в который передается контекст,
            по умолчанию (если не указывать template_name) находится по пути <имя приложения>/<имя модели>_list.html
        context - это данные которые передаются в шаблон. Представляет собой словарь.
            В словаре имеются два поля (значения), к этим полям можно обращатся напрямую из шаблона.
            Поля имеют следующие имена:
                'view' - экзкмпляр нашего класа представления, в данном случае "ProductsInCategoryList"
                'object_list' или знчение из переменной context_object_name - это queryset объект полученный
                    из модели данных, путем выполнения запроса из self.get_queryset() или self.queryset.
                    Queryset - это последовательность в которой содержится результат выполнения запроса к БД,
                    т.е. экземпляры класса model (BlogArticle)
        Для передачи доплнительных данных в шаблон можно использовать следующие подходы, помимо get_queryset:
            1. Класс с методами, методы возвращают данные (например queryset).
                затем этот класс подмешивается (mixin) к нашему представлению
                и данные методы становятся доступными в template (django_movie_shots  - 17)
            2. Использовать get_context_data использование расписано ниже в классе
            3. Использовать simple tags (django_movie_shots  - 15)
            4. Определить метод в модели (django_movie_shots  - 10)
        paginate_by включает пагинацию
    """
    model = BlogArticle
    context_object_name = 'blogArticles'
    allow_empty = False
    # Отключаем пагинацию
    # paginate_by = 3
    # template_name = 'appProductItem/productitem_list.html'

    def get_queryset(self):
        """
            Для получения данных из модели для передачи в контекст используется переменная
            queryset = BlogArticle.objects.all() 
            или метод получения записей get_queryset()
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