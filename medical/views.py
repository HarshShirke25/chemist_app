from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def medindex(request):
    return render(request,"medical/home.html")

@login_required
def order(request):
    return render(request,"medical/order.html")

@login_required
def inven(request):
    return render(request,"medical/inven.html")

@login_required
def info(request):
    return render(request,"medical/info.html")
