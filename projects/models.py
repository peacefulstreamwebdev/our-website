from django.db import models
from django.contrib.auth.models import User
import uuid


class Project(models.Model):
    """
    Model for Projects
    """
    name = models.CharField(max_length=254)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    repo = models.CharField(max_length=254)

    def __str__(self):
        return self.name