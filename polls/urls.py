from django.conf.urls import url
from django.urls import path
from . import views
from web import views as web_views
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    url(r'^home/$', web_views.home, name='home'),
]