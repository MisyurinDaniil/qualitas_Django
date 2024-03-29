# Generated by Django 4.0.5 on 2023-10-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProductItem', '0004_review_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product_url',
            field=models.URLField(default='https:\\qualitas.store', max_length=255, verbose_name='URL товара'),
        ),
        migrations.AlterField(
            model_name='review',
            name='ip',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Ip adress клиента'),
        ),
    ]
