from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^login/$', auth_views.login, {'template_name': 'profile_app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'profile_app/logged_out.html'}, name='logout'),
    url(r'^profile/$', views.profile_edit, name='profile'),
]