from django.shortcuts import render

# Create your views here.

def faq(request):
    '''A view to return the FAQ page'''

    context = {
        'page': 'faq',
    }

    return render(request, 'faq/faq.html', context)