from django.contrib import admin
from django.urls import path
from django import views
from .import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.Userindex,name="Userindex"),
    path('stocks',views.stocks,name="stocks"),
    path('medicalstores',views.medicalstores,name="medicalstores"),
    path('userinfo',views.userinfo,name="userinfo")
   
]