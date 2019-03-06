from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView

from projects.models import Project


class HomeView(generic.TemplateView):
    template_name = "projects.html"
