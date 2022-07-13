from django.shortcuts import render
from contact.models import Content
from .models import Project, ProjectCategory

# Create your views here.

def portfolio(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()

    context = {
        'page': 'portfolio',
        'contact': contact,
        'projects': projects,
        'categories': categories,
    }

    return render(request, 'portfolio/portfolio.html', context)