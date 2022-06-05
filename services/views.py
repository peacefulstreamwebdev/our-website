from django.shortcuts import render
from contact.models import Content
from .models import Service

# Create your views here.

def services(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]
    services = Service.objects.all()

    context = {
        'page': 'services',
        'contact': contact,
        'services': services,
    }

    return render(request, 'services/services.html', context)