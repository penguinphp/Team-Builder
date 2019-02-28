from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView


class HomeView(generic.TemplateView):
    template_name = "index.html"
