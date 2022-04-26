from django.urls import path
from . import views

urlpatterns = [
    path('about-us/', views.about, name='about'),
    path('our-team/', views.team, name='team'),
    path('testimonials/', views.testimonials, name='testimonials'),
]