import os
from django import template

# Создадим экземпляр класса Library() для регистрации пользовательских шаблонных тегов
register = template.Library()

@register.simple_tag()
def is_this_a_subdomain():
    siteaname = os.environ['SITENAME']
    return len(siteaname.split('.')) >= 3

# siteaname = os.environ['SITENAME']
# is_this_a_subdomain = len(siteaname.split('.')) >= 3
# print(is_this_a_subdomain)