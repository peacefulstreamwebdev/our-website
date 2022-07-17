from django.shortcuts import render, get_object_or_404
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


def portfolio_detail(request, item_id):

    project = get_object_or_404(Project, pk=item_id)
    contact = Content.objects.all()[0]

    context = {
        'page': 'portfolio',
        'contact': contact,
        'project': project,
    }

    return render(request, 'portfolio/portfolio-detail.html', context)