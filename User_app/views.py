
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from medical.models import medical,MedStocks
from . models import ordersInfo,userInfo
from django.contrib.auth.models import User
import datetime


@login_required
def Userindex(request):
    
    return render(request,'index.html')

@login_required
def stocks(request):
    if request.method == "GET":
        user1 = User.objects.get(username=request.user.username)
        ords = ordersInfo.objects.filter(user = user1)
    return render(request,'user/stocks.html',{
        'ords':ords
    })
    
    
@login_required
def userinfo(request):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        if userInfo.objects.filter(user = user).exists():
            user1 = userInfo.objects.get(user=user)
            return render(request,"user/userInfo.html",{               
               'user1':user1
             })
        else:
            return render(request,"user/userInfo.html")
            
        
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        if userInfo.objects.filter(user=user).exists():
            us_info = userInfo.objects.get(user=user)
            us_info.name = request.POST['name_user']
            us_info.address = request.POST['add']
            us_info.contact = request.POST['cont']
            us_info.save()
            return redirect("userinfo")
        else:
            name = request.POST['name_user']
            address = request.POST['add']
            contact = request.POST['cont']
            u = userInfo(user=user,name=name,contact=contact,address=address)
            u.save()
            return redirect("userinfo")
    return render(request,"user/userInfo.html")

@login_required
def medicalstores(request):
    if request.method == "GET":
        user1 = User.objects.get(username=request.user.username)
        medicals = medical.objects.all()
        return render(request,"user/medicalstores.html",{
        'medicals':medicals
      })

@login_required     
def medinfo(request,pk):
    
    if request.method == "GET":
        med = medical.objects.get(id = pk)
        med_stocks = MedStocks.objects.filter(user = med.user)
        return render(request,"user/med_info.html",{
            'med' : med,
            'med_stocks':med_stocks
        })
        

@login_required        
def buymed(request,pk):
    og_price=0
    
    if medical.objects.filter(id = pk).exists():
        med = medical.objects.get(id = pk)
    if request.method == "GET":
        user1 = User.objects.get(username=request.user.username)
        med = medical.objects.get(id = pk)
        med_stocks = MedStocks.objects.filter(user = med.user)
        ords = ordersInfo.objects.filter(user=user1,med=med)
       
        return render(request,"user/buymed.html",{
            'med':med,
            'med_stocks':med_stocks,
            'ords':ords,
            
        })
        
    if request.method == "POST":
        user1 = User.objects.get(username=request.user.username)
        med = medical.objects.get(id = pk)
        med_stocks = MedStocks.objects.filter(user = med.user)
        u = userInfo.objects.get(user=user1)
        fname = u.name
        medicine = request.POST.get('medicine')
        quantity = request.POST.get('quantity')
        
        for med_stock in med_stocks:
            if medicine == med_stock.name:
                og_price = med_stock.price
                med_stock.quantity = int(med_stock.quantity)-int(quantity)
                med_stock.save()
        price = int(og_price)*int(quantity)
        ords = ordersInfo(user=user1,med=med,name=medicine,quantity=quantity,price=price,fname=fname)
        ords.save()
        return redirect("buymed",med.id)
    
@login_required        
def order(request,pk):
    total = 0
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        med = medical.objects.get(id = pk)
        ords = ordersInfo.objects.filter(user=user,med=med)
        for ord in ords:
            total = total + ord.price
        u = userInfo.objects.get(user=user)
        date1 = datetime.datetime.now()
        return render(request,"user/order_details.html",{
            'ords':ords,
            'med':med,
            'u':u,
            'date':date1,
            'total':total
        })
    
    
        
    