from django.shortcuts import render
from .models import TeamMember, SkillsContent, Skills, TeamContent, Client, AboutContent, Testimonial
from contact.models import Content
from django.conf import settings

# Create your views here.

def about(request):
    '''A view to return the home page'''

    members = TeamMember.objects.all()
    skills = Skills.objects.all()
    skills_content = SkillsContent.objects.all()[0]
    team_content = TeamContent.objects.all()[0]
    clients = Client.objects.all()
    about_content = AboutContent.objects.all()[0]

    context = {
        'page': 'about',
        'members': members,
        'skills_content': skills_content,
        'skills': skills,
        'team_content': team_content,
        'clients': clients,
        'about_content': about_content,
    }

    return render(request, 'about/about.html', context)


def team(request):
    '''A view to return the home page'''

    members = TeamMember.objects.all()
    team_content = TeamContent.objects.all()[0]

    context = {
        'page': 'about',
        'members': members,
        'team_content': team_content,
    }

    return render(request, 'about/team.html', context)


def testimonials(request):
    '''A view to return the home page'''

    testimonials = Testimonial.objects.all()

    context = {
        'page': 'about',
        'testimonials': testimonials,
    }

    return render(request, 'about/testimonials.html', context)