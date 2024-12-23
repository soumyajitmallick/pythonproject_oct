from django.urls import path
from faculty.views import viewquestion,addsubject,addchapter,addquestion,submitquestion,fhome



urlpatterns=[
    
    path('viewquestion',viewquestion,name="viewquestion"),
    path('addsubject',addsubject,name="addsubject"),
    path('addchapter',addchapter,name="addchapter"),
    path('addquestion',addquestion,name="addquestion"),
    path('submitquestion',submitquestion,name="submitquestion"),  
    path('fhome',fhome,name="fhome"),
]