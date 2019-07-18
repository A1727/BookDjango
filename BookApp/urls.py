from django.urls import path
from django.contrib import admin
from BookApp import views

urlpatterns = [
    path('', views.store),
]


