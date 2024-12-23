from django.shortcuts import render
from .models import register_master

# Create your views here.
def register(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        pwd=request.POST.get("password")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        role=request.POST.get("role")
        ob=register_master.objects.create(name=name,mobile=mobile,email=email,password=pwd,gender=gender,dob=dob,role=role)
        ob.save()
        return render(request,"register.html",{"result":"register sucessfull..."})
    return render(request,'register.html')