from django.urls import path
from BookApp import views

urlpatterns = [
    path('index/', views.index),
    path('store/', views.store),
]