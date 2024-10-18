from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('integer/', views.integer, name="integer"),
    path('recycle/', views.recycle, name="recycle")
]
