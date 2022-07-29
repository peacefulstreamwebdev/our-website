from django.shortcuts import render
from .models import Content, BlackList
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm

# Create your views here.

def contact(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]

    if request.method == "POST":
        form = ContactForm(request.POST)
        form_data = request.body.decode().split("=")
        name = form_data[2].split('&')[0].replace('%20', ' ')
        user_email = form_data[3].split('&')[0].replace('%40', '@')
        subject = form_data[4].split('&')[0].replace('%20', ' ').replace('%2C', ',')
        message = form_data[5].split('&')[0].replace('%20', ' ').replace('%2C', ',').replace('%0D%0A', '\n')

        try:
            blacklisted_user = BlackList.objects.get(name=name)
        except:
            blacklisted_user = False

        try:
            blacklisted_email = BlackList.objects.get(email=user_email)
        except:
            blacklisted_email = False

        if blacklisted_user or blacklisted_email:
            pass
        else:
            contact_notification_message = render_to_string(
                'contact/emails/contact_email.txt', {
                    'name': name,
                    'user_email': user_email,
                    'subject': subject,
                    'message': message,
                }
            )

            contact_notification_message_wrapper = EmailMessage(
                f'New Website Contact: {name}',
                contact_notification_message,
                to=[settings.DEFAULT_TO_EMAIL]
            )

            contact_notification_message_wrapper.send()

    else:
        form = ContactForm()

    context = {
        'page': 'contact',
        'contact': contact,
        'form': form,
    }

    return render(request, 'contact/contact.html', context)