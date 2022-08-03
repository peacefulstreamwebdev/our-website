from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('add/', views.add_project, name='add_project'),
    path('active/', views.active_projects, name='active_projects'),
    path('<str:project_id>/', views.project, name='project'),
]