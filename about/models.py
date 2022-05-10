from tokenize import blank_re
from django.db import models

# Create your models here.

class TeamContent(models.Model):

    name = models.CharField(max_length=254)
    team_content_blurb = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):

    name = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name