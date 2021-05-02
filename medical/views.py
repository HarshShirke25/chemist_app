from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import medical,MedStocks
import datetime

# Create your views here.

@login_required
def medindex(request):
    return render(request,"medical/home.html")

@login_required
def order(request):
    return render(request,"medical/order.html")

@login_required
def inven(request):
    if request.method == "GET":
        user1 = User.objects.get(username=request.user.username)
        stock_infos = MedStocks.objects.filter(user=user1)
        date = datetime.datetime.now()
        return render(request,"medical/inven.html",{
            'stock_infos':stock_infos,
            'date':date
        })
    if request.method == "POST":
        user1 = User.objects.get(username=request.user.username)
        nameMedicine = request.POST['nameMedicine']
        quantity = request.POST['quantity']
        
        m = MedStocks(user=user1,name=nameMedicine,quantity=quantity)
        m.save()
        return redirect("inventory")
        
    return render(request,"medical/inven.html")

@login_required
def info(request):
    if request.method == "GET":
        user1 = User.objects.get(username=request.user.username)
        med_info = medical.objects.get(user=user1)
        return render(request,"medical/info.html",{
            'med_info':med_info
        })
    if request.method == "POST":
        user1 = User.objects.get(username=request.user.username)
        name_of_med = request.POST['name_of_med']
        address = request.POST['address']
        contact = request.POST['contact']
        reg_num = request.POST['reg_num']
        est = request.POST['est']
        med = medical(user=user1,name_of_med=name_of_med,address=address,contact=contact,reg_num=reg_num,est=est)
        med.save()
        return render(request,"medical/info.html")
    return render(request,"medical/info.html")
