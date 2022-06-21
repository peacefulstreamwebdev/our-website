from django.shortcuts import render
from contact.models import Content
from .models import Service, Feature
from .models import Content as FeatureContent

# Create your views here.

def services(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]
    services = Service.objects.all()
    feature = Feature.objects.all()
    feature_content = FeatureContent.objects.all()[0]

    context = {
        'page': 'services',
        'contact': contact,
        'services': services,
        'feature_content': feature_content,
        'features': feature,
    }

    return render(request, 'services/services.html', context)