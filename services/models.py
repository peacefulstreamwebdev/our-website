from django.db import models
from tables import Description

# Create your models here.

class Service(models.Model):

    name = models.CharField(max_length=254)
    icon_color = models.CharField(max_length=254, null=True, blank=True)
    icon_class = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(max_length=1200)

    def __str__(self):
        return self.name