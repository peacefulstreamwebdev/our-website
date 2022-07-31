from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserForm
from allauth.account.models import EmailAddress

# Create your views here.

@login_required
def me(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(User, username=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        form_two = UserForm(request.POST, instance=user)
        if form.is_valid() and form_two.is_valid():
            try:
                user_email = get_object_or_404(EmailAddress, user_id=request.user)
                if str(request.POST.get('email')) != str(user_email):
                    new_email = request.POST.get('email')
                    profile.add_email_address(request, new_email)
                else:
                    pass
                form.save()
                form_two.save()
            except EmailAddress.MultipleObjectsReturned:
                pass
        else:
            pass
    else:
        form = UserProfileForm(instance=profile)
        form_two = UserForm(instance=user)

    context = {
        'user': user,
        'profile': profile,
    }

    return render(request, 'profiles/me.html', context)


@login_required
def edit_profile(request):
    """ Edit the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(User, username=request.user)

    form = UserProfileForm(instance=profile)
    form_two = UserForm(instance=user)

    template = 'profiles/edit_profile.html'
    
    context = {
        'form': form,
        'form_two': form_two,
    }

    return render(request, template, context)