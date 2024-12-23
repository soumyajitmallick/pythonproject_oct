from django.shortcuts import render,redirect
from Register.models import register_master
# Create your views here.

def viewdata(request):
    ob=register_master.objects.all()
    if request.method=="POST":
        email=request.POST["email"]
        btn=request.POST['btn']
        if btn=="edit":
            obj=register_master.objects.filter(email=email)
            return render(request,'edit.html',{'data':obj})
        if btn=="delete":
            obj=register_master.objects.filter(email=email).delete()
            ob=register_master.objects.all()
            return render(request,'viewdata.html',{'data':ob})
    return render(request,'viewdata.html',{'data':ob})

def update(request):
    if request.method=="POST":        
        name=request.POST["name"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        pwd=request.POST['pwd']
        role=request.POST['role']
        try:
            ob=register_master.objects.filter(email=email).update(name=name,mobile=mobile,password=pwd,role=role)
            obj=register_master.objects.all()
            # return render(request,"viewdata.html",{'data':obj})
            return redirect('viewdata')
        except Exception as e:
            return render(request,"viewdata.html")

    return render(request,'viewdata.html')


def login(request):
    if request.method=="POST":
        email=request.POST["email"]
        pwd=request.POST["pwd"]
        try:
            ob=register_master.objects.get(email=email,password=pwd)
            request.session["name"]=ob.name
            request.session["email"]=ob.email
            request.session["mobile"]=ob.mobile
            request.session["gender"]=ob.gender
            request.session["role"]=ob.role

            if ob.status==1:

                if ob.role=="student":
                    return redirect('shome')
            
                elif ob.role=="admin":
                    return redirect('ahome')
            
                elif ob.role=="faculty":
                    return redirect("fhome")
            
                elif ob.role=="staff":
                    return redirect('staffhome')
                else:
                    return redirect('login')
                
            elif ob.status==0:
                return render(request,'login.html',{"msg":"waiting for admin confirmassion...."})
        
        except Exception as e:
            return render(request,"login.html",{"msg":"invalid userid & password..." + str(e)})
    return render(request,"login.html")