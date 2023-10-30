from django import template
from qualitas.settings import DEBUG

# Получаем состояние переменной DEBUG для вкл/откл скрипта Yandex.Metrika counter

# Создадим экземпляр класса Library() для регистрации пользовательских шаблонных тегов
register = template.Library()

# используем декоратор simple_tag() для создания (регистрации) функции ввиде тега
@register.simple_tag()
def getDebugInfo():
    return DEBUG

