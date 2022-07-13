from django.shortcuts import render
from contact.models import Content
from services.models import Service
from portfolio.models import Project, ProjectCategory
from about.models import Client
from .models import SlideContent

# Create your views here.

def home(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]
    services = Service.objects.all()
    slides = SlideContent.objects.all()
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
    clients = Client.objects.all()

    context = {
        'page': 'home',
        'contact': contact,
        'services': services,
        'slides': slides,
        'projects': projects,
        'categories': categories,
        'clients': clients,
    }

    return render(request, 'home/home.html', context)