from django import forms
from .models import Position, Project, Application


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'timeline', 'requirements', 'skills', ]


class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ['name', 'description', 'skills', ]


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('applicant', 'position', 'status')
        widgets = {'applicant': forms.HiddenInput,
                   'position': forms.HiddenInput,
                   'status': forms.HiddenInput}



