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

    captcha = ReCaptchaField()
    
    class Meta:
        model = Review
        fields = ("stars", "userName", "text", "captcha", 'product_url')

