from django.shortcuts import render
from contact.models import Content

# Create your views here.

def portfolio(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]

    context = {
        'page': 'portfolio',
        'contact': contact,
    }

    return render(request, 'portfolio/portfolio.html', context)