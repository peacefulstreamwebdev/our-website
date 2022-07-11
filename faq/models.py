from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class FaqCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Faq(models.Model):

    name = models.CharField(max_length=254)
    category = models.ForeignKey('FaqCategory', null=True, blank=True, on_delete=models.SET_NULL)
    question = models.CharField(max_length=500)
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)
    answer = models.TextField(max_length=2000)
    tags = TaggableManager()

    def __str__(self):
        return self.name