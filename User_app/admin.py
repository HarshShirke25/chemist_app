from django.contrib import admin
from . models import userInfo,ordersInfo

# Register your models here.

admin.site.register(userInfo)
admin.site.register(ordersInfo)