from django.db import models
from about.models import Client

# Create your models here.

class ProjectCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Project(models.Model):

    name = models.CharField(max_length=254)
    image = models.ImageField()
    image_two = models.ImageField(null=True, blank=True)
    image_three = models.ImageField(null=True, blank=True)
    category = models.ForeignKey('ProjectCategory', null=True, blank=True, on_delete=models.SET_NULL)
    link = models.URLField(max_length=254, null=True, blank=True)
    date_completed = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    project_title = models.CharField(max_length=254)
    project_description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name