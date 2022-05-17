from django.shortcuts import render
from contact.models import Content

# Create your views here.

def home(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]

    context = {
        'page': 'home',
        'contact': contact,
    }

    return render(request, 'home/home.html', context)