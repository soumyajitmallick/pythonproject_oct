from django.shortcuts import render,redirect
from Register.models import register_master
from .models import *


# Create your views here.
def staffhome(request):
    name=request.session.get("name")

    ob=register_master.objects.filter(role='staff')
    obj1=register_master.objects.filter(role='student')
    obj=register_master.objects.filter(role='faculty')
    return render(request,"staffhome.html",{"staffname":name,"staffdata":ob, "fdata":obj, "sdata":obj1})



def addbook(request):
    if request.method == "POST":
        bname = request.POST['bname']
        aname = request.POST['aname']
        isbnno = request.POST['isbnno']

        ob=add_Book.objects.create(Book_Name=bname,Author_Name=aname,ISBN_No=isbnno)
        ob.save()

        return render(request,"addBook.html",{"msg":'Book added successfully!'})

    return render(request, 'addBook.html')  

def viewbook(request):
    obj = add_Book.objects.all()

    if request.method == "POST":
        btn = request.POST.get('btn')
        isbnno = request.POST.get('ISBN_No')

        # Handle "delete" action
        if btn == "delete":
            add_Book.objects.filter(ISBN_No=isbnno).delete()
            return redirect('viewbook')

        # Handle "save" action
        elif btn == "save":
            book = add_Book.objects.get(ISBN_No=isbnno)
            book.Book_Name = request.POST.get('Book_Name')
            book.Author_Name = request.POST.get('Author_Name')
            book.ISBN_No = request.POST.get('ISBN_No') 
            book.save()
            return redirect('viewbook')


        elif btn == "edit":
        
            return render(request, 'viewBook.html', {'viewbook': obj,'edit_isbn': isbnno   })

    return render(request, 'viewBook.html', {'viewbook':obj})

def issuebook(request):
    ob=add_Book.objects.all()
    obj=register_master.objects.all()
    if request.method=="POST":
        bookname=request.POST['bookname']
        mobile=request.POST['mobile']
        bname=add_Book.objects.get(Book_Name=bookname)
        obbook=Book_Issued.objects.create(Book_Name=bname,mobile=mobile)
        obbook.save()
        return redirect('issuebook')
    return render(request,'issueBook.html',{'obbook':ob,'obmobile':obj})

# def issuedbookview(request):
#     ob= Book_Issued.objects.all()
#     return render(request,'issuedBookview.html',{'viewbookissue':ob})
 
def issuedbookview(request):
    ob=Book_Issued.objects.all()
    if request.method == "POST":
        btn = request.POST.get('btn')
        if btn == "Cancel" :
                book_id=request.POST['book_id']
                Book_Issued.objects.get( Book_Issued_id=book_id).delete()
                return redirect('issuedbookview')
        
    return render(request,'issuedbookview.html',{'viewbookissue':ob})