from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
   if request.user.is_anonymous:
       return redirect("/login")
   return render(request,'index.html')
    
def loginuser(request):
    if request.method == "POST":
        email = request.POST.get('eamil')
        password = request.POST.get('password')
        # print(email,password)

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'login.html')
    return render(request,'login.html')
    
def logoutuser(request):
    logout(request)
    return redirect("/login")
    
