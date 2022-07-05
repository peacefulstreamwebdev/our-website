from django.db import models

# Create your models here.

class SlideContent(models.Model):

    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=254)
    blurb = models.TextField(max_length=1000)

    def __str__(self):
        return self.name