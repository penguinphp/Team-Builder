from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"new/$", views.ProjectCreate.as_view(), name="new_project"),
    url(r"detail/(?P<project_pk>\d+)/$", views.project_detail, name="project_detail"),
    url(r"detail/(?P<project_pk>\d+)/add/postion$", views.add_position, name="position_create"),
    url(r"edit/(?P<pk>\d+)/$", views.EditProject.as_view(), name="edit_project"),
    url(r"^delete/(?P<pk>\d+)/$", views.DeleteProject.as_view(), name="delete_project"),
    url(r"^apply/(?P<position_pk>\d+)/$", views.ApplyView.as_view(), name="apply"),
    url(r"applications/$", views.applications, name="applications"),
    url(r"applications/accepted/$", views.accepted_applications, name="accepted_applications"),
    url(r"applications/(?P<app_pk>\d+)/(?P<status>accepted|rejected)/$", views.accept_or_reject, name="accept_reject"),
    ]