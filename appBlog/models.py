from django.db import models
from django.urls import reverse


class BlogArticle(models.Model):
    '''
        Класс модели статьи блога
    '''
    name = models.CharField(max_length=255, verbose_name='Название статьи (заголовок h1)')
    autor = models.CharField(max_length=255, verbose_name='Автор статьи')
    autor_photo = models.ImageField(upload_to='blog_img/',
                                    default='img/blog/blog-author.png',
                                    verbose_name='Фото автора')
    description = models.TextField(verbose_name='Описание при выборе статьи')
    is_published = models.BooleanField(default=True, verbose_name='Разрешить публикацию')
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name='URL (формирует автоматически из "Наименование товара")')
    page_title = models.CharField(verbose_name='Заголовок страницы браузера (<title>)', max_length=80)
    page_description = models.TextField(verbose_name='Описание страницы SEO (description)', max_length=200)
    page_keywords = models.CharField(verbose_name='Ключевые слова SEO (keywordss)', max_length=255)
    img_main_small = models.ImageField(upload_to='blog_img/', verbose_name='Основное фото 400х267')
    img_main_small_alt = models.CharField(verbose_name='Атрибут alt основного фото', max_length=80)
    img_main_small_title = models.CharField(verbose_name='Атрибут title основного фото', max_length=80)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_active_big_header = models.BooleanField(default=False,
                                               verbose_name='Включить большую шапку сайта с большой картинкой')
    img_header_mobile = models.ImageField(upload_to='blog_img/',
                                          verbose_name='Фото шапки - mobile 576х568 (необяз. поле)',
                                          default='',
                                          blank=True)
    img_header_mobile_horizontal = models.ImageField(upload_to='blog_img/',
                                                     verbose_name='Фото шапки - mobile 768х568 (необяз. поле)',
                                                     default='',
                                                     blank=True)
    img_header_tablet = models.ImageField(upload_to='blog_img/',
                                          verbose_name='Фото шапки - tablet 1200х550 (необяз. поле)',
                                          default='',
                                          blank=True)
    img_header_desktop = models.ImageField(upload_to='blog_img/',
                                           verbose_name='Фото шапки - desktop 1440х760 (необяз. поле)',
                                           default='',
                                           blank=True)
    alt_img_header = models.CharField(verbose_name='Атрибут alt фото шапки (необяз. поле)',
                                      max_length=80,
                                      blank=True)
    title_img_header = models.CharField(verbose_name='Атрибут title фото шапки (необяз. поле)',
                                        max_length=80,
                                        blank=True)
    text_aticle = models.TextField(verbose_name='Текст статьи')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''
            Генерируем динамическую ссылку для блога
        '''
        return reverse('finalblogpage', kwargs={'blogPageSlug': self.slug})

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Статьи блога"
