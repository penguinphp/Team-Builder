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
        url(r'^change-avatar/$', views.change_avatar, name='change_avatar'),
        url(r'^change-skills/$', views.change_skills, name='change_skills'),
        url(r'^profile/(?P<pk>\d+)/$', views.show_any_profile, name="any_profile"),
]
