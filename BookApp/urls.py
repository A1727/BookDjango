from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from BookApp import views

urlpatterns = [
    path('', views.store),
    url(r'^book/(\d+)', views.book_details, name='book_details'),
]


