from django.shortcuts import render

# Create your views here.

def portfolio(request):
    '''A view to return the home page'''

    context = {
        'page': 'portfolio',
    }

    return render(request, 'portfolio/portfolio.html', context)