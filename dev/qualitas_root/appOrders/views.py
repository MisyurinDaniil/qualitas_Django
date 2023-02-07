from django.shortcuts import render

from django.http import HttpResponse
from .models import Order
from appProductItem.models import ProductItem
from appTelegram.sendmessage import sendTelegram
# Create your views here.


def makeorder(request):
    newOrder = Order()

    product_id = request.POST['product_id']
    customer_name = request.POST['customer_name']
    customer_telephone = request.POST['customer_telephone']
    customer_comment = request.POST['customer_comment']
    product_name = ProductItem.objects.get(pk=product_id).product_name
    # Получаем ДНС имя сервера "qualitas.store"
    # server_url = request.META['HTTP_HOST']
    # server_url = request.get_host()
    get_full_path = request.POST['get_full_path']

    text = ('ID товара - ' + product_id + '\n' + 
            'Ссылка на товар - ' + get_full_path + '\n' + 
            'Название товара - ' + product_name + '\n' + 
            'Имя заказчика - ' + customer_name + '\n' + 
            'Телефон закачика - ' + customer_telephone + '\n' + '\n' +
            'Комментарий к заказу - ' + customer_comment)

    newOrder.order_binding = ProductItem.objects.get(pk=product_id)
    newOrder.order_customer_name = customer_name
    newOrder.order_customer_telephone = customer_telephone
    newOrder.order_customer_comment = customer_comment
    newOrder.order_product_url = get_full_path
    newOrder.save()

    sendTelegram(text)

    return HttpResponse("True")