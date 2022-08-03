from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Project, Stage
from django.contrib import messages
from .forms import AddProjectForm
import requests
import os
import datetime

# Create your views here.

@login_required
def all_projects(request):
    """View for projects page"""

    if request.user.is_superuser:
        projects = Project.objects.all()
        heading = 'All Projects'
    else:
        projects = Project.objects.filter(user=request.user)
        heading = 'My Projects'

    stages = Stage.objects.all()
    template = 'projects/projects.html'
    
    context = {
        'projects': projects,
        'heading': heading,
        'stages': stages,
    }

    return render(request, template, context)


@user_passes_test(lambda user: user.is_superuser)
def active_projects(request):
    """View for active projects page"""

    projects = Project.objects.filter(completed=False)
    heading = 'Active Projects'

    template = 'projects/projects.html'
    
    context = {
        'projects': projects,
        'heading': heading,
    }

    return render(request, template, context)


@user_passes_test(lambda user: user.is_superuser)
def add_project(request):
    """View for add projects page"""

    if request.method == 'POST':
        form = AddProjectForm(request.POST)
        form.name = request.POST["name"]
        form.user = request.POST["user"]
        form.repo = request.POST["repo"]
        form.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect(reverse('home'))
    else:
        form = AddProjectForm()

    template = 'projects/add_project.html'
    
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def project(request, project_id):
    """View for single project"""

    project = get_object_or_404(Project, project_id=project_id)
    stages = Stage.objects.filter(project=project).order_by('target_date')

    if stages:
        owner = os.environ.get('GITHUB_OWNER')
        token = os.environ.get('GITHUB_TOKEN')
        url = f'https://api.github.com/repos/{ owner }/{ project.repo }/commits'
        headers = {'Authorization': f'token {token}'}
        
        try:
            commit = requests.get(url, headers=headers).json()[0]
            date = datetime.datetime.strptime(commit['commit']['author']['date'], "%Y-%m-%dT%H:%M:%SZ") - datetime.timedelta(hours=4)
            date.strftime('%b %d, %Y, %H:%M EST')
        except:
            commit = None
            date = None

        context = {
            'project': project,
            'stages': stages,
            'commit': commit,
            'date': date,
        }

    else:
        context = {
            'project': project,
            'stages': stages,
        }

    template = 'projects/project.html'

    return render(request, template, context)