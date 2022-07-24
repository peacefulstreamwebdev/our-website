from django.shortcuts import render, get_object_or_404
from contact.models import Content
from .models import Project, ProjectCategory
from django.conf import settings

# Create your views here.

def portfolio(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
    tidio_id = settings.TIDIO_ID

    context = {
        'page': 'portfolio',
        'contact': contact,
        'projects': projects,
        'categories': categories,
        'tidio_id': tidio_id,
    }

    return render(request, 'portfolio/portfolio.html', context)


def portfolio_detail(request, item_id):

    project = get_object_or_404(Project, pk=item_id)
    contact = Content.objects.all()[0]
    tidio_id = settings.TIDIO_ID

    context = {
        'page': 'portfolio',
        'contact': contact,
        'project': project,
        'tidio_id': tidio_id,
    }

    return render(request, 'portfolio/portfolio-detail.html', context)