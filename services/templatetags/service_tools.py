from django import template
from services.models import Service

register = template.Library()

@register.filter(name='services')
def services(all_services):
    all_services = Service.objects.values()
    return all_services