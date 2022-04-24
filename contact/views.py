from django.shortcuts import render

# Create your views here.

def contact(request):
    '''A view to return the home page'''

    context = {
        'page': 'contact',
    }

    return render(request, 'contact/contact.html', context)