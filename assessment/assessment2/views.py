from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Product_Master,Order_Master
from django.contrib import messages
# Create your views here.
def order(request):
    ob=Product_Master.objects.all()
    if request.method=="POST":
        prodid=request.POST["pid"]
        ob1=Product_Master.objects.get(prodID=prodid)
        product = {
            'price' : ob1.prodRate,
            'Qty' : ob1.prodQty}
        return JsonResponse({'prodobj':product})
    return render(request,"order.html", {"obj":ob})


def orderplace(request):
    if request.method=="POST":
        pid=request.POST["pid"]
        prate=request.POST["prate"]
        oqty=request.POST["oqty"]
        ovalue=int(prate)*int(oqty)
        ob=Order_Master.objects.create(prodID=pid,prodRate=prate,orderQty=oqty,orderValue=ovalue)
        ob.save()
        messages.success(request,"Order placed successfully!")
    return redirect("order")