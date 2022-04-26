from django.shortcuts import render

# Create your views here.

def services(request):
    '''A view to return the home page'''

    context = {
        'page': 'services',
    }

    return render(request, 'services/services.html', context)