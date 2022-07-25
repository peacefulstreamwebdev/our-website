from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='tidio')
def tidio(id):
    id = settings.TIDIO_ID
    return id