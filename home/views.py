from django.shortcuts import render
from contact.models import Content
from services.models import Service
from .models import SlideContent

# Create your views here.

def home(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]
    services = Service.objects.all()
    slides = SlideContent.objects.all()

    context = {
        'page': 'home',
        'contact': contact,
        'services': services,
        'slides': slides,
    }

    return render(request, 'home/home.html', context)