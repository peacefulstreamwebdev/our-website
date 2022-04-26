from django.shortcuts import render

# Create your views here.

def about(request):
    '''A view to return the home page'''

    context = {
        'page': 'about',
    }

    return render(request, 'about/about.html', context)


def team(request):
    '''A view to return the home page'''

    context = {
        'page': 'about',
    }

    return render(request, 'about/team.html', context)


def testimonials(request):
    '''A view to return the home page'''

    context = {
        'page': 'about',
    }

    return render(request, 'about/testimonials.html', context)