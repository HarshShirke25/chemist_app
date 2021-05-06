from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import medical,MedStocks
import datetime
from User_app.models import ordersInfo,userInfo

# Create your views here.

@login_required
def medindex(request):
    user1 = User.objects.get(username=request.user.username)
    if medical.objects.filter(user = user1).exists():
        med_info = medical.objects.get(user = user1)
        return render(request,"medical/home.html",{
            'med_info':med_info
        })
    else:
        return render(request,"medical/home.html")
    

@login_required
def order(request):
    if request.method == "GET":
        user1 = User.objects.get(username=request.user.username)
        if medical.objects.filter(user = user1).exists():
            med = medical.objects.get(user=user1)
            ords = ordersInfo.objects.filter(med=med)
            return render(request,"medical/order.html",{
                'ords':ords,
           })
        else:
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
        price = request.POST['price']
        
        m = MedStocks(user=user1,name=nameMedicine,quantity=quantity,price=price)
        m.save()
        return redirect("inventory")
        
    return render(request,"medical/inven.html")

@login_required
def info(request):
    if request.method == "GET":
        user1 = User.objects.get(username=request.user.username)
        if medical.objects.filter(user = user1).exists():
            med_info = medical.objects.get(user=user1)
            return render(request,"medical/info.html",{               
                'med_info':med_info
           })   
        else:
            return render(request,"medical/info.html") 
        
    if request.method == "POST":
        user1 = User.objects.get(username=request.user.username)
        if medical.objects.filter(user=user1).exists():
            med_info = medical.objects.get(user=user1)
            med_info.name_of_med = request.POST['name_of_med']
            med_info.address = request.POST['address']
            med_info.contact = request.POST['contact']
            med_info.reg_num = request.POST['reg_num']
            med_info.est = request.POST['est']
            med_info.save()
            return redirect("info")
        else:
            name_of_med = request.POST['name_of_med']
            address = request.POST['address']
            contact = request.POST['contact']
            reg_num = request.POST.get('reg_num')
            est = request.POST.get('est')
            med = medical(user=user1,name_of_med=name_of_med,address=address,contact=contact,reg_num=reg_num,est=est)
            med.save()
            return redirect("info")
            
        
    return render(request,"medical/info.html")
