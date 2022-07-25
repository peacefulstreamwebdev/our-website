from django.shortcuts import render, get_object_or_404
from contact.models import Content
from .models import Project, ProjectCategory
from django.conf import settings

# Create your views here.

def portfolio(request):
    '''A view to return the home page'''

    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()

    context = {
        'page': 'portfolio',
        'projects': projects,
        'categories': categories,
    }

    return render(request, 'portfolio/portfolio.html', context)


def portfolio_detail(request, item_id):

    project = get_object_or_404(Project, pk=item_id)

    context = {
        'page': 'portfolio',
        'project': project,
    }

    return render(request, 'portfolio/portfolio-detail.html', context)