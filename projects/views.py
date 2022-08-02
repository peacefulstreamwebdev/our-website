from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Project, Stage

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


@login_required
def project(request, project_id):
    """View for single project"""

    project = get_object_or_404(Project, project_id=project_id)
    stages = Stage.objects.filter(project=project).order_by('target_date')

    context = {
        'project': project,
        'stages': stages,
    }

    template = 'projects/project.html'

    return render(request, template, context)