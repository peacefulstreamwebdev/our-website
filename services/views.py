from django.shortcuts import render
from contact.models import Content

# Create your views here.

def services(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]

    context = {
        'page': 'services',
        'contact': contact,
    }

    return render(request, 'services/services.html', context)