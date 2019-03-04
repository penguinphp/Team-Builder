from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"new/$", views.ProjectCreate.as_view(), name="new_project"),
    url(r"detail/(?P<project_pk>\d+)/$", views.project_detail, name="project_detail"),
    url(r"edit/(?P<pk>\d+)/$", views.EditProject.as_view(), name="edit_project"),
    url(r"^delete/(?P<pk>\d+)/$", views.DeleteProject.as_view(), name="delete_project"),
    #url(r"^applications/$", views.Applications.as_view(), name="applications"),
    url(r"(?P<pk>\d+)/position/new/$", views.new_position, name="new_position"),
    ]