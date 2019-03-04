from django import forms

from .models import Position, Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'timeline', 'requirements', 'skills',]


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['project', 'name', 'description',]
