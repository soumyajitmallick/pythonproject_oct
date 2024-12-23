from django.shortcuts import render,redirect
from Register.models import register_master
from django.http import JsonResponse
from .models import *

# Create your views here.
def fhome(request):
    name=request.session.get("name")
    email=request.session.get('email')
    obj=register_master.objects.get(email=email)
    ob=register_master.objects.filter(role='student')

    return render(request,"fhome.html",{"data":obj,"data1":ob, "fname":name})

def viewquestion(request):
    ob=subject.objects.all()
    ob1=chapter.objects.all()
    ob2=question.objects.all()

    return render(request,'viewquestion.html',context={'sub':ob, 'cpt':ob1, 'qsn':ob2})

def addsubject(request):
    if request.method=="POST":
        sub=request.POST["sub"]
        ob=subject.objects.create(subject_name=sub)
        ob.save()
        return render(request,'addsubject.html',{'msg':'subject added successfully'})
    return render(request,'addsubject.html')

def addchapter(request):
    ob=subject.objects.all()
    if request.method=="POST":
        sub_name=request.POST["sub_name"]
        subject_name=subject.objects.get(subject_name=sub_name)
        cpt_name=request.POST["cpt_name"]
        ob1=chapter.objects.create(subject_name=subject_name,chapter_name=cpt_name)
        ob1.save()
        return render(request,"addchapter.html",{"msg":"chapter added sucessfully"})
    return render(request,"addchapter.html",{'subname':ob})

def addquestion(request):
    ob=subject.objects.all()
    if request.method=="POST":
        sub_name=request.POST['sub_name']
        try:
            subject_name=subject.objects.get(subject_name=sub_name)
            ob=chapter.objects.filter(subject_name=subject_name)
            chapter_names=[chapter.chapter_name for chapter in ob]

            return JsonResponse({'data':chapter_names})
        except subject.DoesNotExist:
            return JsonResponse({'data': []})
    return render(request,'addquestion.html',context={'sub':ob})

def submitquestion(request):
    if request.method=="POST":
        a=request.POST["sub_name"]
        sub_name=subject.objects.get(subject_name=a)
        b=request.POST["cpt_name"]
        cpt_name=chapter.objects.get(chapter_name=b)
        qsn =request.POST["qsn"]
        opt1=request.POST["opt1"]  
        opt2=request.POST["opt2"] 
        opt3=request.POST["opt3"] 
        opt4=request.POST["opt4"] 
        answer=request.POST["answer"] 
        ob=question.objects.create(subject_name=sub_name,chapter_name=cpt_name,question=qsn,option1=opt1,option2=opt2,option3=opt3,option4=opt4,answer=answer)
        ob.save()
        return redirect("addquestion")
    return render(request,'addquestion.html')
