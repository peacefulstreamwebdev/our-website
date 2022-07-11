from django.shortcuts import render
from .models import Faq

# Create your views here.

def faq(request):
    '''A view to return the FAQ page'''

    faqs = Faq.objects.all()

    context = {
        'page': 'faq',
        'faqs': faqs,
    }

    return render(request, 'faq/faq.html', context)