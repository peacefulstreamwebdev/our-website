from django.shortcuts import render
from .models import Content

# Create your views here.

def contact(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]

    context = {
        'page': 'contact',
        'contact': contact,
    }

    return render(request, 'contact/contact.html', context)