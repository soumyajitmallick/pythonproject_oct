from django.shortcuts import render,HttpResponse
from .models import contact
from .models import add
# Create your views here.

# to return through HttpResponse
def index(request):
    return HttpResponse("<h1>Welcome to seeree </h1>")

# to return through render
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,"about.html")

def contact_details(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        message=request.POST["message"]
        ob=contact.objects.create(name=name,email=email,mobile=mobile,message=message)
        ob.save()
        return render(request,"contact.html",{"result":"Message send successfully.."})
    return render(request,'contact.html')

def faqs(request):
    return render(request,"faqs.html")

def add(request):
    if request.method=="POST":
        fno=int(request.POST["f1"])
        sno=int(request.POST["f2"])
        operation = request.POST.get("operation", "add")

        if operation == "add":
            result=fno+sno
            
        elif operation == "sub":
            result=fno-sno

        elif operation == "mul":
            result=fno*sno

        elif operation == "div":
            result=fno/sno

        print(result)
        return render (request,'add.html',{"output":result})
    return render(request,'add.html')

#Create your views here
    