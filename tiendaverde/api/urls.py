from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('integer/', views.integer, name="integer"),
    path('recycle/', views.recycle, name="recycle"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('addcart/', views.addcart, name="addcart"),
    path('removecart/', views.removecart, name="removecart"),
    path('purchase/', views.purchase, name="buy")
]
