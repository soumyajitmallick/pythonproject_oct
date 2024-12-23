from django.shortcuts import render
from signup .models import signup_master
from user .models import Transaction
# Create your views here.

def deposite_withdraw(request):
    account_no=request.session.get('account_no')
    ob=signup_master.objects.get(account_no=account_no)
    if request.method=="POST":
        amount=request.POST['amt']
        print(request.POST)
        if request.POST['TransactionType']=="Deposit":
            type="Deposit"
            obj=Transaction.objects.create(account_no=ob,amount=amount,type=type)
            obj.save()
            return render(request,'transation.html',{'msg':f'{type} successfully' }) 
        else:
            type='Withdraw'
            obj=Transaction.objects.create(account_no=ob,amount=amount,type=type)
            obj.save()
            return render(request,'transation.html',{'msg':f'{type} successfully'})
    return render(request,'transation.html')

def current_balance(request):
    account_no = request.session.get('account_no')
    ob = signup_master.objects.get(account_no=account_no)
    obj = Transaction.objects.filter(account_no=ob)
    total_deposit = sum(item.amount for item in obj if item.type == 'Deposit')
    total_withdraw = sum(item.amount for item in obj if item.type == 'Withdraw')
    current_balance=int(total_deposit-total_withdraw)
    return render(request, 'current_balance.html', {'data': obj,'balance':current_balance, 'total_deposit': total_deposit,"total_withdraw":total_withdraw,})


def balance_details(request):
    account_no=request.session.get('account_no')
    ob=signup_master.objects.get(account_no=account_no)
    obj=Transaction.objects.filter(account_no = ob)[::-1]
    total_deposit = sum(item.amount for item in obj if item.type == 'Deposit')
    return render(request,'balance_history.html', {'total_deposit':total_deposit,'data':obj,'data1':ob})


def userhome(request):
    name=request.session.get('name')
    account_no=request.session.get('account_no')
    email=request.session.get("email")
    mobile=request.session.get("mobile_no")
    return render(request,'userhome.html', {'email':email,'mobile_no':mobile,'name':name,'account_no':account_no})
    