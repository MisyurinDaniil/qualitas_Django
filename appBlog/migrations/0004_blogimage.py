# Generated by Django 4.0.5 on 2023-11-17 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0003_alter_blogarticle_autor_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_medium', models.ImageField(upload_to='blog_img/', verbose_name='Средное фото 570х380')),
                ('img_big', models.ImageField(upload_to='blog_img/', verbose_name='Большое фото 1280х853')),
                ('img_alt', models.CharField(max_length=80, verbose_name='Атрибут alt фото')),
                ('img_title', models.CharField(max_length=80, verbose_name='Атрибут title фото')),
                ('blog_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBlog.blogarticle', verbose_name='Статья блога')),
            ],
            options={
                'verbose_name': 'Картинка стать блога',
                'verbose_name_plural': 'Картинки статей блога',
            },
        ),
    ]
