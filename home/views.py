from django.shortcuts import render
from contact.models import Content
from services.models import Service
from portfolio.models import Project, ProjectCategory
from about.models import Client, AboutContent
from .models import SlideContent
from django.conf import settings

# Create your views here.

def home(request):
    '''A view to return the home page'''

    services = Service.objects.all()
    slides = SlideContent.objects.get_queryset().order_by('id')
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
    clients = Client.objects.all()
    about_content = AboutContent.objects.all()[0]

    context = {
        'page': 'home',
        'services': services,
        'slides': slides,
        'projects': projects,
        'categories': categories,
        'clients': clients,
        'about_content': about_content,
    }

    return render(request, 'home/home.html', context)