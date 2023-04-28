from django.shortcuts import render

from django.http import HttpResponse
from .models import Order
from .forms import ReviewForm
from appProductItem.models import ProductItem
from appTelegram.sendmessage import sendTelegram

from django.views.generic.base import View
# Create your views here.

class Makeorder(View):
        def post(self, request, pk):
                form = ReviewForm(request.POST)
                print(form)
                print(request.POST)
                print(pk)
                form.order_binding = pk
                print(form.is_valid())
                print(form.cleaned_data)
                print(form.errors)
                # if form.is_valid():
                #         form.save()
                # print(form.__dict__)
                # if form.is_valid():
                #         form = form.save()
                        # print(request)
                        # print(request.__dict__)
                return HttpResponse("True")

# def makeorder(request):
#     newOrder = Order()

#     product_id = request.POST['product_id']
#     customer_name = request.POST['customer_name']
#     customer_telephone = request.POST['customer_telephone']
#     customer_comment = request.POST['customer_comment']
#     product_name = ProductItem.objects.get(pk=product_id).product_name
#     # Получаем ДНС имя сервера "qualitas.store"
#     # server_url = request.META['HTTP_HOST']
#     # server_url = request.get_host()
#     get_full_path = request.POST['get_full_path']

#     text = ('ID товара - ' + product_id + '\n' + 
#             'Ссылка на товар - ' + get_full_path + '\n' + 
#             'Название товара - ' + product_name + '\n' + 
#             'Имя заказчика - ' + customer_name + '\n' + 
#             'Телефон закачика - ' + customer_telephone + '\n' + '\n' +
#             'Комментарий к заказу - ' + customer_comment)

#     newOrder.order_binding = ProductItem.objects.get(pk=product_id)
#     newOrder.order_customer_name = customer_name
#     newOrder.order_customer_telephone = customer_telephone
#     newOrder.order_customer_comment = customer_comment
#     newOrder.order_product_url = get_full_path
#     newOrder.save()

#     sendTelegram(text)

#     return HttpResponse("True")