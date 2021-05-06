from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.contrib import auth,messages
from .utils import have_group
from django.contrib.auth import logout


# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request,"auth/login.html")
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if username and password:
            user = auth.authenticate(username=username,password=password)
            if user:
                if have_group(user,"MEDICAL"):
                    auth.login(request,user)
                    messages.success(request,"Logged In Successfully!")
                    return redirect('orders')
                elif have_group(user,"USER"):
                    auth.login(request,user)
                    messages.success(request,"Logged In Successfully")
                    return redirect('medicalstores')
        else:
            messages.error(request,"Enter all fields")
            return render(request,"auth/login.html")
                  
    return render(request,"auth/login.html")

def registerMed(request):
    if request.method == "GET":
        return render(request,"auth/med_register.html")
    
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username,email,password)
        my_group = Group.objects.get_or_create(name="MEDICAL")
        my_group[0].user_set.add(user)
        user.save()
        
    return render(request,"auth/login.html")

def registerUser(request):
    if request.method == "GET":
        return render(request,"auth/registration.html")
    
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username,email,password)
        my_group = Group.objects.get_or_create(name="USER")
        my_group[0].user_set.add(user)
        user.save()
    return render(request,"auth/login.html")

def logout(request):
    auth.logout(request)
    messages.success(request,"Successfully Logged out")
    return redirect('login')
    
    
