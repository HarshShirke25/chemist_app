from django.contrib import admin
from django.urls import path
from django import views
from .import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.medindex,name="medindex"),
    path('orders',views.order,name="orders"),
    path('inventory',views.inven,name="inventory"),
    path('info',views.info,name="info")
]