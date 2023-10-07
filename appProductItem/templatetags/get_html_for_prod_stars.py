from django import template

# Получаем все категории товара для nav-left

# Создадим экземпляр класса Library() для регистрации пользовательских шаблонных тегов
register = template.Library()

# используем декоратор inclusion_tag() для создания (регистрации) функции ввиде тега
@register.inclusion_tag('appProductItem/production_stars.html')
def getHtmlForProdStars(starsNuber = 0):
    return {"starsNuber": starsNuber,}
