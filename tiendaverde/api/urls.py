from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('integer/<int:id>/', views.integer, name="integer")
]
