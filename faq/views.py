from django.shortcuts import render, redirect, reverse
from .models import Faq, FaqCategory
from taggit.models import Tag
from django.db.models import Q

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

    query = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            faqs = faqs.filter(category__name__in=categories)
            categories = FaqCategory.objects.filter(name__in=categories)

        if 'tags' in request.GET:
            tags = request.GET['tags'].split(',')
            faqs = faqs.filter(tags__name__in=tags)
            tags = Tag.objects.filter(name__in=tags)

        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                return redirect(reverse('faq'))
            
            queries = Q(question__icontains=query) | Q(answer__icontains=query)
            faqs = faqs.filter(queries)

    context = {
        'page': 'faq',
        'faqs': faqs,
        'tags': tags,
        'category_data': zip(categories, lengths),
        'search_term': query,
    }

    return render(request, 'faq/faq.html', context)