# Generated by Django 4.0.5 on 2023-10-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProductItem', '0005_review_product_url_alter_review_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product_url',
            field=models.URLField(default='https://qualitas.store/', max_length=255, verbose_name='URL товара'),
        ),
    ]