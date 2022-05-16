from django.shortcuts import render
from .models import TeamMember

# Create your views here.

def about(request):
    '''A view to return the home page'''

    members = TeamMember.objects.all()

    context = {
        'page': 'about',
        'members': members,
    }

    return render(request, 'about/about.html', context)


def team(request):
    '''A view to return the home page'''

    members = TeamMember.objects.all()

    context = {
        'page': 'about',
        'members': members,
    }

    return render(request, 'about/team.html', context)


def testimonials(request):
    '''A view to return the home page'''

    context = {
        'page': 'about',
    }

    return render(request, 'about/testimonials.html', context)