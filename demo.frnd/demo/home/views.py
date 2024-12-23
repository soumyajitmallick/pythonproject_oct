from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = userMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reg')
    formobj = userMasterForm()
    ob = UserMaster.objects.all()[::-1]
    return render(request, 'register.html',{'form':formobj, 'obj':ob})


def login(request):
    return render(request, 'login.html')
