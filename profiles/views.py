from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def me(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(User, username=request.user)

    context = {
        'user': user,
        'profile': profile,
    }

    return render(request, 'profiles/me.html', context)