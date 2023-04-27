from django import forms

from .models import Order


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Order
        fields = ("order_binding", "order_product_url", "order_customer_name", "order_customer_telephone", "order_customer_comment")
