from django import forms
from .models import Project, Stage
import os
import requests

class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = (
            'project_id',
            'date_created',
            'progress',
            'last_updated',
            'latest_update',
            'completed',
        )
        

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Project Name',
            'user': 'User',
            'repo': 'Github Repo',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False


class AddStageForm(forms.ModelForm):
    class Meta:
        model = Stage
        exclude = ('date_updated',)
        

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'progress': '0',
            'latest_update': 'Latest Update',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False