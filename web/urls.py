from django.conf.urls import url
from django.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^home/$', views.home, name='home'),
]