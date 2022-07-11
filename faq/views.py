from django.shortcuts import render
from .models import Faq, FaqCategory
from taggit.models import Tag

# Create your views here.

def faq(request):
    '''A view to return the FAQ page'''

    faqs = Faq.objects.all()
    tags = Tag.objects.all()
    categories = FaqCategory.objects.all()

    lengths = []
    for category in categories:
        length = len(faqs.filter(category=category.id))
        lengths.append(length)

    context = {
        'page': 'faq',
        'faqs': faqs,
        'tags': tags,
        'category_data': zip(categories, lengths),
    }

    return render(request, 'faq/faq.html', context)