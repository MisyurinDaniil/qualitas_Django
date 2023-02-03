from django import template
from appProductItem.models import ProductCategory

# Получаем все категории товара для nav-left

# Создадим экземпляр класса Library() для регистрации пользовательских шаблонных тегов
register = template.Library()

# используем декоратор simple_tag() для создания функции ввиде тега
@register.simple_tag()
def getProductsCategorys():
    return ProductCategory.objects.filter(product_category_is_published = True)