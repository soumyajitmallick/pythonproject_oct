from django.shortcuts import render
from .models import signup_master
# Create your views here.

def signup(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        pwd=request.POST['pwd']
        mobile=request.POST['mobile']
        ob=signup_master.objects.create(user_name=name,email=email,password=pwd,mobile_no=mobile)
        ob.save()
        return render(request,'signup.html',{'msg':'Register sucessfull...'})
    return render(request,'signup.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')