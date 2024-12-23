from django.shortcuts import render
from Register.models import register_master
from faculty.models import *
from django.http import JsonResponse

# Create your views here.
def shome(request):
    name=request.session.get("name")
    email=request.session.get('email')
    ob=register_master.objects.get(email=email)

    return render(request,"shome.html",{"data":ob, "sname":name})

def exam(request):
    ob=subject.objects.all()
    ob1=chapter.objects.all()
    ob2=question.objects.all()
    return render(request,'exam.html',context={'sub':ob,'cpt':ob1,'qsn':ob2})

def get_questions(request):
    if request.method=="POST":
        sub_name=request.POST['sub_name']
        sub=subject.objects.get(subject_name=sub_name)
        cpt_name=request.POST['cpt_name']
        cpt=chapter.objects.get(chapter_name=cpt_name)
        questions=question.objects.filter(subject_name=sub,chapter_name=cpt)
        return render(request,'question.html',{'questions':questions})
    return render(request,'question.html')

from .models import question

def submit_answers(request):
    if request.method == "POST":
        answers = {}
        for question in question.objects.all():
            # Capture the answer submitted for each question, dynamically based on question ID
            answer = request.POST.get(f'answer_{question.id}')
            if answer:
                answers[question.id] = answer
        # Process the answers (e.g., compare with correct answers, store results, etc.)
        # You can return a response, such as showing a result page
        return render(request, 'result.html', {'answers': answers},{"msg":"Answer Submitted"})
    
    # If the form is not submitted, render the form again
    questions = question.objects.all()
    return render(request, 'result.html', {'questions': questions})
def evaluate ( request ) :
    result = 0
    if request.method =='POST' :
        for qstn in request.POST :
            try :
                if question.objects.get(question_id = int(qstn)).answer == request.POST [qstn] :
                    #load this record in ans table (sid,qid,ans)
                    result += 1
            except :
                pass
    return render (request,'success.html',{'result':result})                

