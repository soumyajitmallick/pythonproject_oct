from django.shortcuts import render,redirect
from signup.models import signup_master
# Create your views here.
def login(request):
    if request.method=="POST":
        email=request.POST["email"]
        pwd=request.POST["pwd"]
        ob=signup_master.objects.get(email=email,password=pwd)
        request.session["name"]=ob.user_name
        request.session["email"]=ob.email
        request.session["mobile_no"]=ob.mobile_no
        request.session["account_no"]=ob.account_no
        if ob.status==1:
            return redirect('userhome')
        else:
            msg="Waiting for the admin conformation....!!!"
            return render(request,'login.html',{'msg':msg})
    return render(request,'login.html')