from django.contrib import admin
from django.urls import path
from django import views
from .import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/',views.login,name="login"),
    path('registerUser/',views.registerUser,name="registerUser"),
    path('registerMed/',views.registerMed,name="registerMed"),
    path('logout/',views.logout,name="logout")
     
]