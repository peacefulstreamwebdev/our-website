from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
import random
import string
import os
import requests


class Stage(models.Model):
    """
    Model for Stages
    """
    name = models.CharField(max_length=254)
    project = models.ForeignKey('Project', null=True, blank=True, on_delete=models.SET_NULL)
    progress = models.IntegerField(null=True, blank=True)
    target_date = models.DateField(null=True, blank=True)
    latest_update = models.TextField(max_length=2000, null=True, blank=True)
    date_updated = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Model for Projects
    """
    project_id = models.CharField(max_length=16, null=False, editable=False)
    name = models.CharField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    repo = models.CharField(max_length=254)
    date_created = models.DateField(auto_now_add=True)
    progress = models.IntegerField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    latest_update = models.TextField(max_length=2000, null=True, blank=True)
    completed = models.BooleanField(default=False)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        output_string = ''.join(random.SystemRandom().choice(string.ascii_letters.lower() + string.digits) for _ in range(16))
        return output_string

    def update_progress(self):
        stages = Stage.objects.filter(project=self)
        progress = 0
        for stage in stages:
            progress = progress + stage.progress
        self.progress = progress / len(stages)
        latest_updated_stage = stages.latest('date_updated')
        self.last_updated = latest_updated_stage.date_updated
        self.latest_update = latest_updated_stage.latest_update
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.project_id:
            self.project_id = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Stage)
def latest_date_updated(sender, instance, **kwargs):
    """
    Create or update the user profile
    """
    if instance.latest_update != None:
        instance.date_updated = timezone.now()
    else:
        pass


@receiver(post_save, sender=Stage)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.project.update_progress()