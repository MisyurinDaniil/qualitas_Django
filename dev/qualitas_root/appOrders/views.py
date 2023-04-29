from django.http import HttpResponse
from .forms import ReviewForm
from appProductItem.models import ProductItem
from appTelegram.sendmessage import sendTelegram

from django.views.generic.base import View
# Create your views here.

class Makeorder(View):
        def post(self, request, pk):
                form = ReviewForm(request.POST)
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
                return HttpResponse("False")