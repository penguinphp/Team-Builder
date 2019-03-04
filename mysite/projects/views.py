from django.shortcuts import render
from .forms import ProjectForm, PositionForm
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Project, Position, Application
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectCreate(LoginRequiredMixin, CreateView):
    form_class = ProjectForm
    template_name = "new_project.html"
    queryset = Project.objects.all()

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ProjectCreate, self).form_valid(form)


class EditProject(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['title', 'description', 'requirements', 'timeline', 'skills',]

    def form_valid(self, form):
        if form.instance.owner == self.request.user:
            return super(EditProject, self).form_valid(form)


class DeleteProject(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("home")


def project_detail(request, project_pk):
    project = Project.objects.get(id=project_pk)
    positions = project.positions.all()
    return render(request, 'project_detail.html', {'project': project, 'positions': positions})


def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def new_position(request, project_pk):
    project = Project.objects.get(id=project_pk)
    form = PositionForm(request.POST)

    if request.method == 'POST':
        position = form.save(commit=False)
        position.project = project
        form.save()
        return redirect('projects:project_detail',  project_pk=project.id)

    else:
        form = PositionForm()
        args = {'form': form}
        return render(request, 'new_position.html', args)


def apply_for_project(request, position_pk):
    position = Position.objects.get(id=position_pk)
    project = position.project
    application = Application.objects.filter(
        applicant=request.user,
        position=position,
    )


