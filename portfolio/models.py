from django.db import models

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
    category = models.ForeignKey('ProjectCategory', null=True, blank=True, on_delete=models.SET_NULL)
    link = models.URLField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name