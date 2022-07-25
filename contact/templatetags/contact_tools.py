from django import template
from contact.models import Content

register = template.Library()

@register.filter(name='contact')
def contact(contact_info):
    contact_info = Content.objects.all()
    return contact_info