from django.shortcuts import render
from django.db.models import Q
from .models import BlogArticle
from django.views.generic import ListView, DetailView


def blog_page(request):
    return render(request, './appBlog/blogarticle_list.html')


def finalblogpage_page(request):
    return render(request, './appBlog/finalblogpage.html')


class BlogList(ListView):
    """
        https://proproprogs.ru/django/klassy-predstavleniy-listview-detailview-createview
        model = /MyModel Class for ListView/ - поле с сслылкой на модель данных.
        По умолчанию в контекст попадают все элементы модели переданной в переменную model,
            эквивалента записи MyModel.objects.all(), если не указвать def get_queryset() или queryset
        allow_empty = False - генерирует исключение 404 если список статей пуст
        template_name = Шаблон в который передается контекст, по умолчанию
            (если не указывать поле template_name) находится по пути <имя приложения>/<имя модели>_list.html
        context - это данные которые передаются в шаблон. Представляет собой словарь.
            В словаре имеются два поля (значения), к этим полям можно обращатся напрямую из шаблона.
            Поля имеют следующие имена:
                'view' - экзкмпляр нашего класа представления MyClass(ListView)
                'object_list' или можно поменять имя этой переменной через присвоение значения
                    полю context_object_name (значение - строка в нижнем регистре).
                    В поле object_list хранится queryset, который является
                    значением возвращенным из запроса из метода self.get_queryset() или поля self.queryset.
                    Queryset - это последовательность в которой содержится результат выполнения запроса к БД,
                    т.е. экземпляры класса model = /MyModel Class for ListView/
        Для передачи доплнительных данных в шаблон можно использовать следующие подходы, помимо get_queryset:
            1. Класс с методами, методы возвращают данные (например queryset).
                затем этот класс подмешивается (mixin) к нашему представлению
                и данные методы становятся доступными в template (django_movie_shots  - 17)
            2. Использовать get_context_data использование расписано ниже в классе
            3. Использовать simple tags (django_movie_shots  - 15)
            4. Определить метод в модели (django_movie_shots  - 10)
        paginate_by = 3 - включает пагинацию
    """
    model = BlogArticle
    context_object_name = 'blogarticles'
    # allow_empty = False

    def get_queryset(self):
        """
            Для получения данных из модели для передачи в контекст используется переменная
            queryset = MyModel.objects.all()
            или метод получения записей def get_queryset()
        """
        return BlogArticle.objects.all().filter(Q(is_published=True))


class BlogDetail(DetailView):
    """
        При попытке просмотра какого-либо поста, возникает исключение «AttributeError».
            В чем проблема? Смотрите, вот этот класс DetailView по умолчанию пытается
            выбрать из указанной модели ProductItem запись, используя атрибут pk или slug.
            Но у нас формируется маршрут с параметром productItemSlug из-за этого и возникает такая ошибка.
            Используем переменную slug_url_kwarg = 'productItemSlug' для обозначения своей переменной slug
            или ее нужно изменить в url.conf
        slug_url_kwarg - имя перемонной содержащей slug из url.conf
        slug_field-  Имя поля в модели, которое содержит slug. По умолчанию slug_field - 'slug'.
    """
    model = BlogArticle
    context_object_name = 'blogarticle'
    slug_url_kwarg = 'blogPageSlug'
    slug_field = 'slug'

    def get_object(self):
        try:
            return BlogArticle.objects.get((Q(is_published=True)) & Q(slug=self.kwargs['blogPageSlug']))
        except (BlogArticle.DoesNotExist):
            from django.http import Http404
            raise Http404()
