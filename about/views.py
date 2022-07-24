from django.shortcuts import render
from .models import TeamMember, SkillsContent, Skills, TeamContent, Client, AboutContent, Testimonial
from contact.models import Content
from django.conf import settings

# Create your views here.

def about(request):
    '''A view to return the home page'''

    members = TeamMember.objects.all()
    skills = Skills.objects.all()
    contact = Content.objects.all()[0]
    skills_content = SkillsContent.objects.all()[0]
    team_content = TeamContent.objects.all()[0]
    clients = Client.objects.all()
    about_content = AboutContent.objects.all()[0]
    tidio_id = settings.TIDIO_ID

    context = {
        'page': 'about',
        'members': members,
        'contact': contact,
        'skills_content': skills_content,
        'skills': skills,
        'team_content': team_content,
        'clients': clients,
        'about_content': about_content,
        'tidio_id': tidio_id,
    }

    return render(request, 'about/about.html', context)


def team(request):
    '''A view to return the home page'''

    members = TeamMember.objects.all()
    contact = Content.objects.all()[0]
    tidio_id = settings.TIDIO_ID

    context = {
        'page': 'about',
        'members': members,
        'contact': contact,
        'tidio_id': tidio_id,
    }

    return render(request, 'about/team.html', context)


def testimonials(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]
    testimonials = Testimonial.objects.all()
    tidio_id = settings.TIDIO_ID

    context = {
        'page': 'about',
        'contact': contact,
        'testimonials': testimonials,
        'tidio_id': tidio_id,
    }

    return render(request, 'about/testimonials.html', context)