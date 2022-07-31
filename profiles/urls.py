from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.me, name='me'),
    path('edit/', views.edit_profile, name='edit_profile')
]