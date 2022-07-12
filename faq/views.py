from django.shortcuts import render, redirect, reverse
from .models import Faq, FaqCategory
from contact.models import Content
from taggit.models import Tag
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def faq(request):
    '''A view to return the FAQ page'''

    contact = Content.objects.all()[0]
    faqs = Faq.objects.get_queryset().order_by('id')
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

    paginator = Paginator(faqs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page': 'faq',
        'contact': contact,
        'faqs': faqs,
        'tags': tags,
        'category_data': zip(categories, lengths),
        'search_term': query,
        'page_obj': page_obj,
    }

    return render(request, 'faq/faq.html', context)