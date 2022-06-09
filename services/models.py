from django.db import models

# Create your models here.

class Service(models.Model):

    name = models.CharField(max_length=254)
    icon_color = models.CharField(max_length=254, null=True, blank=True)
    icon_class = models.CharField(max_length=254, null=True, blank=True)
    svg_path = models.CharField(max_length=3000)
    description = models.TextField(max_length=1200)

    def __str__(self):
        return self.name


class Content(models.Model):

    name = models.CharField(max_length=254)
    features_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Feature(models.Model):

    name = models.CharField(max_length=254)
    icon_color = models.CharField(max_length=254, null=True, blank=True)
    icon_class = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name