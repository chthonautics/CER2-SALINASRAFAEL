from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('store/', views.store, name="store"),
    path('form/', views.form, name="form")
]
