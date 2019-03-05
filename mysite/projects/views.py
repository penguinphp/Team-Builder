from django.shortcuts import render
from .forms import ProjectForm, PositionForm, ApplicationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from notifications.signals import notify
from django.contrib import messages
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Project, Position, Application
from django.contrib.auth.mixins import LoginRequiredMixin


skill = ['Android Developer', 'Designer', 'Java Developer', 'PHP Developer', 'Python Developer',
          'Rails Developer', 'Wordpress Devloper', 'iOS Developer',]


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
    position = project.positions.all()
    return render(request, 'project_detail.html', {'project': project, 'position': position})


def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def add_position(request, project_pk):
    project = Project.objects.get(id=project_pk)
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            position = form.save(commit=False)
            position.project = project
            position.save()
            return redirect('projects:project_detail', project_pk=project.id)
    else:
        form = PositionForm()
        args = {'form': form}
    return render(request, 'new_position.html', args)


class ApplyView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ApplicationForm
    model = Application
    template_name = "new_app.html"
    success_url = reverse_lazy("home")

    def get_initial(self, **kwargs):
        return {'position': self.kwargs.get('position_pk'),
                'applicant': self.request.user,
                'status': 'p'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['position_name'] = Position.objects.get(
            id=self.kwargs.get('position_pk')
        ).name
        return context

    def form_valid(self, form):
        position = Position.objects.get(id=self.kwargs.get('position_pk'))
        applicant = self.request.user
        self.object = form.save()
        messages.success(self.request, 'You have applied for the position!')
        return HttpResponseRedirect(self.get_success_url())
















def applications(request):
    apps = Application.objects.filter(
        position__project__owner=request.user)
    return render(request, 'applications.html', {'apps': apps})
