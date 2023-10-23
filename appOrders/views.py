from django.http import HttpResponse
from .forms import OrderForm
from appProductItem.models import ProductItem
from django.views.generic.base import View
from qualitas.settings import telegram_token, telegram_chat_id
# Create your views here.

# Перед использование request, необходимо установить библиотекуц request

import requests

# Имя используемого бота @QualitasLeather_SuperBot


def sendTelegram(text = 'Test'):
    api = 'https://api.telegram.org/bot'
    method = api + telegram_token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': telegram_chat_id,
        'text' : text,
    })
#     print(telegram_token, telegram_chat_id)
#     print(text)


# sendTelegram()


class Makeorder(View):
    def post(self, request, pk):
        form = OrderForm(request.POST)
        if form.is_valid():
                # Изменять форму можно только после команды form = form.save(commit=False)
                form = form.save(commit=False)
                form.order_binding_id = pk
                form.save()
                text = ('Ссылка на товар - ' + request.POST['order_product_url'] + '\n' + 
                        'Название товара - ' + ProductItem.objects.get(id=pk).product_name + '\n' + 
                        'Имя заказчика - ' + request.POST['order_customer_name'] + '\n' + 
                        'Телефон закачика - ' + request.POST['order_customer_telephone'] + '\n' + '\n' +
                        'Комментарий к заказу - ' + request.POST['order_customer_comment'])
                sendTelegram(text)
                return HttpResponse("True")
        print(form.errors)
        return HttpResponse("False")