from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from BookApp import views
import debug_toolbar

urlpatterns = [
    path('', views.store),
    url(r'^book/(\d+)', views.book_details, name='book_details'),
    url(r'^add/(\d+)', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(\d+)', views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/', views.cart, name='cart'),
    path('_debug_/',include(debug_toolbar.urls)),
]


