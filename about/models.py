from django.db import models
from sympy import matrix_multiply_elementwise

# Create your models here.

class AboutContent(models.Model):

    name = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    heading = models.CharField(max_length=254)
    paragraph = models.TextField(max_length=2000)
    bullet_one = models.CharField(max_length=254)
    bullet_two = models.CharField(max_length=254)
    bullet_three = models.CharField(max_length=254)

    def __str__(self):
        return self.name


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


class SkillsContent(models.Model):

    name = models.CharField(max_length=254)
    skills_content_blurb = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class Skills(models.Model):

    name = models.CharField(max_length=254)
    skill = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Client(models.Model):

    name = models.CharField(max_length=254)
    client = models.ImageField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):

    name = models.CharField(max_length=254)
    role = models.CharField(max_length=254)
    testimonial = models.TextField(max_length=2000)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
