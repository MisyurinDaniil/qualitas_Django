# Generated by Django 4.0.5 on 2023-11-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название статьи')),
                ('autor', models.CharField(max_length=255, verbose_name='Автор статьи')),
                ('autor_photo', models.ImageField(default='img/blog/blog-author.png', upload_to='blog_img/', verbose_name='Фото автора')),
                ('description', models.TextField(verbose_name='Описание при выборе статьи')),
                ('is_published', models.BooleanField(default=True, verbose_name='Разрешить публикацию')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL (формирует автоматически из "Наименование товара")')),
                ('page_title', models.CharField(max_length=80, verbose_name='Заголовок страницы браузера (<title>)')),
                ('page_description', models.TextField(max_length=200, verbose_name='Описание страницы SEO (description)')),
                ('page_keywords', models.CharField(max_length=255, verbose_name='Ключевые слова SEO (keywordss)')),
                ('img_main_small', models.ImageField(upload_to='blog_img/', verbose_name='Основное фото 400х267')),
                ('img_main_small_alt', models.CharField(max_length=80, verbose_name='Атрибут alt основного фото')),
                ('img_main_small_title', models.CharField(max_length=80, verbose_name='Атрибут title основного фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('is_active_big_header', models.BooleanField(default=False, verbose_name='Включить большую шапку сайта с большой картинкой')),
                ('img_header_mobile', models.ImageField(blank=True, default='', upload_to='blog_img/', verbose_name='Фото шапки - mobile 576х568 (не обяз. поле)')),
                ('img_header_mobile_horizontal', models.ImageField(blank=True, default='', upload_to='blog_img/', verbose_name='Фото шапки - mobile 768х568 (не обяз. поле)')),
                ('img_header_tablet', models.ImageField(blank=True, default='', upload_to='blog_img/', verbose_name='Фото шапки - tablet 1200х550 (не обяз. поле)')),
                ('img_header_desktop', models.ImageField(blank=True, default='', upload_to='blog_img/', verbose_name='Фото шапки - desktop 1440х760 (не обяз. поле)')),
                ('alt_img_header', models.CharField(max_length=80, verbose_name='Атрибут alt фото шапки (не обяз. поле)')),
                ('title_img_header', models.CharField(max_length=80, verbose_name='Атрибут title фото шапки (не обяз. поле)')),
                ('text_aticle', models.TextField(verbose_name='Текст статьи')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Статьи блога',
            },
        ),
    ]
