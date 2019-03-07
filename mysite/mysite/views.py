from django.views import generic

from projects.models import Project


class HomeView(generic.TemplateView):
    template_name = "projects.html"
