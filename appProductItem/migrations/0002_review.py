# Generated by Django 4.0.5 on 2023-10-07 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appProductItem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.SmallIntegerField(default=0, verbose_name='Количество звезд рейтинга')),
                ('userName', models.CharField(max_length=255, verbose_name='Имя пользователся')),
                ('text', models.TextField(max_length=2000, verbose_name='Текст отзыва')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата отзыва')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProductItem.productitem', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]