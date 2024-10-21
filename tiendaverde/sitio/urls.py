from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('store/', views.store, name="store"),
    path('form/', views.form, name="form"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="login"),
    path('account/', views.account, name="account"),
    #path('test/', views.test, name="test"),
]
