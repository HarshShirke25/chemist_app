
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from medical.models import medical,MedStocks
from django.contrib.auth.models import User


@login_required
def Userindex(request):
    return render(request,'index.html')

@login_required
def stocks(request):
    return render(request,'user/stocks.html')

def userinfo(request):
    return render(request,"user/userInfo.html")

def medicalstores(request):
    if request.method == "GET":
        user1 = User.objects.get(username=request.user.username)
        medicals = medical.objects.all()
        return render(request,"user/medicalstores.html",{
        'medicals':medicals
      })
        
def medinfo(request,pk):
    if medical.objects.filter(id = pk).exists():
        med = medical.objects.get(id = pk)
    if request.method == "GET":
        med = medical.objects.get(id = pk)
        med_stocks = MedStocks.objects.filter(user = med.user)
        return render(request,"user/med_info.html",{
            'med' : med,
            'med_stocks':med_stocks
        })
    
        
    