from django.contrib import admin

# Register your models here.

from .models import Order
# Register your models here.

class CustomizeOrder(admin.ModelAdmin):
    # Кортеж с именами полей, который хотим отобразит в админ панеле на этапе просмотра всего перечня заказов
    list_display = ('id', 'order_binding', 'order_customer_name', 'order_date')
    # Отмечаем поля по нажатию на которые можно перейти на страницу заказа
    list_display_links = ('id', 'order_binding', 'order_customer_name', 'order_date')
    # Указжем поля отображаемые на карточке заказа
    fields = ('id', 'order_binding', 'order_date', 'order_customer_name', 'order_customer_telephone', 'order_customer_comment', 'order_product_url')
    # Если не задать параметр readonly_fields? django выдаст ошибку, т.к. поле order_date и id не изменяемые
    readonly_fields = ('id', 'order_binding', 'order_date')
    # Укажем сколько строк на одной странице
    list_per_page = 10
    # Укажем максимальное количество полей при выводе всех
    list_max_show_all = 100

admin.site.register(Order, CustomizeOrder)