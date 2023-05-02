from django import template
from women.models import *


register = template.Library()




@register.inclusion_tag('women/TagsTemplates/menu.html')
def get_menu(user=None):
    menu = [
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
    ]
    if user and user.is_staff:
        menu.append({'title': "Добавить статью", 'url_name': 'add_page'})
    return {'menu': menu}
