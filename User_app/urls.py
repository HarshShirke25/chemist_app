from django.contrib import admin
from django.urls import path
from django import views
from .import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('registration',views.registration,name="registration"),
    path('stocks',views.stocks,name="stocks")
   
]