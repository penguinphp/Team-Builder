from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
        url(r'^register/$', views.register, name='register'),
        url(r"logout/$", views.logout_view, name="logout"),
        url(r'^login/$', views.login_view, name='login'),
        url(r'^profile/$', views.my_profile, name='profile'),
        url(r'^edit/$', views.edit_profile, name='edit'),
        url(r'^change-password/$', views.change_password, name='change_password'),
]
