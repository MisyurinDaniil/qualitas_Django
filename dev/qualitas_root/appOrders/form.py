from django import forms

from .models import Order


class ReviewForm(forms.ModelForm):
    """
        Форма отзывов

        Для указания класса для поля input можно использовать следующую конструкцию
        def __init__(self, *args, **kwargs):
            super(ReviewForm, self).__init__(*args, **kwargs)
            self.fields['order_customer_name'].widget.attrs['class'] = 
    """

    class Meta:
        model = Order
        fields = ("order_binding", "order_product_url", "order_customer_name", "order_customer_telephone", "order_customer_comment")
        widgets = {
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
