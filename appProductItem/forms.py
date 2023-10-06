from django import forms
from .models import Review

# Проект recapcha на github
# Там же находится мануал
# https://github.com/kbytesys/django-recaptcha3

# Для корректной работы recaptcha3 необходимо в файле 
# /venv/lib/python3.10/site-packages/snowpenguin/django/recaptcha3/fields.py
# заменить
# from django.utils.translation import ugettext_lazy as _
# to:
# from django.utils.translation import gettext_lazy as _
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

class AddReviewForm(forms.ModelForm):
    """
        Форма отзывов

        Для указания класса для поля input можно использовать следующую конструкцию
        def __init__(self, *args, **kwargs):
            super(AddReviewForm, self).__init__(*args, **kwargs)
            self.fields['order_customer_name'].widget.attrs['class'] = 
    """
    captcha = ReCaptchaField()
    
    class Meta:
        model = Review
        fields = ("userName", "text", "stars", "product", "captcha")
        # labels = {
        #     'order_customer_name': 'Как вас зовут', 
        #     'order_customer_telephone': 'Контактный телефон',
        #     'order_customer_comment': 'Комментарий к заказу'
        #     }
        widgets = {
            'order_product_url': forms.URLInput(attrs =
                {
                    'class': 'display-none',
                }),
            'order_customer_name': forms.TextInput(attrs =
                {
                    'class': 'modal-window__input',
                    'placeholder': 'Имя',
                }),
            'order_customer_telephone': forms.TextInput(attrs =
                {
                    'class': 'modal-window__input',
                    'placeholder': 'Номер телефона',
                }),
            'order_customer_comment': forms.Textarea(attrs =
                {
                    'class': 'modal-window__input',
                    'placeholder': 'Комментарий',
                    'cols': '20',
                    'rows': '5',
                }),
        }
