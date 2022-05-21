from django.shortcuts import render
from .models import TeamMember, SkillsContent, Skills
from contact.models import Content

# Create your views here.

def about(request):
    '''A view to return the home page'''

    members = TeamMember.objects.all()
    skills = Skills.objects.all()
    contact = Content.objects.all()[0]
    skills_content = SkillsContent.objects.all()[0]

    context = {
        'page': 'about',
        'members': members,
        'contact': contact,
        'skills_content': skills_content,
        'skills': skills,
    }

    return render(request, 'about/about.html', context)


def team(request):
    '''A view to return the home page'''

    members = TeamMember.objects.all()
    contact = Content.objects.all()[0]

    context = {
        'page': 'about',
        'members': members,
        'contact': contact,
    }

    return render(request, 'about/team.html', context)


def testimonials(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]

    context = {
        'page': 'about',
        'contact': contact,
    }

    return render(request, 'about/testimonials.html', context)