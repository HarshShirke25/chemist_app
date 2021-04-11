
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def Userindex(request):
    return render(request,'index.html')

@login_required
def stocks(request):
    return render(request,'user/stocks.html')

def userinfo(request):
    return render(request,"user/userInfo.html")

def medicalstores(request):
    return render(request,"user/medicalstores.html")