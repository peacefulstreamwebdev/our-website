from django.shortcuts import render
from .models import Content
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.

def contact(request):
    '''A view to return the home page'''

    contact = Content.objects.all()[0]

    if request.method == "POST":
        form_data = request.body.decode().split("=")
        name = form_data[2].split('&')[0].replace('%20', ' ')
        user_email = form_data[3].split('&')[0].replace('%40', '@')
        subject = form_data[4].split('&')[0].replace('%20', ' ').replace('%2C', ',')
        message = form_data[5].split('&')[0].replace('%20', ' ').replace('%2C', ',').replace('%0D%0A', '\n')

        contact_notification_message = render_to_string(
            'contact/emails/contact_email.txt', {
                'name': name,
                'user_email': user_email,
                'subject': subject,
                'message': message,
            }
        )

        contact_notification_message_wrapper = EmailMessage(
            f'Hey Peaceful Stream Development! {name} is trying to contact you from your website!',
            contact_notification_message,
            to=[settings.DEFAULT_TO_EMAIL]
        )

        contact_notification_message_wrapper.send()

    context = {
        'page': 'contact',
        'contact': contact,
    }

    return render(request, 'contact/contact.html', context)