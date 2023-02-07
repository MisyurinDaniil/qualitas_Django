from django.db import models

# Create your models here.

from appProductItem.models import ProductItem

# Create your models here.

class Order(models.Model):
    order_binding = models.ForeignKey(ProductItem, on_delete=models.PROTECT, verbose_name='Ссылка на покупаемый товар')
    order_product_url = models.CharField(max_length=255, verbose_name='URL товара')
    order_date = models.DateTimeField(auto_now=True, verbose_name='Дата заказа')
    order_customer_name = models.CharField(max_length=255, verbose_name='Имя заказчика')
    order_customer_telephone= models.CharField(max_length=255, verbose_name='Телефон заказчика')
    order_customer_comment= models.TextField(verbose_name='Комментарий к заказу')

    def __str__(self):
        return self.order_binding.product_name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"