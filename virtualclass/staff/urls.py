from django.urls import path
from staff.views import staffhome,addbook,viewbook,issuebook,issuedbookview



urlpatterns=[
    path('staffhome',staffhome,name="staffhome"),
    path('addbook',addbook,name="addbook"),
    path('viewbook',viewbook,name="viewbook"),
    path('issuebook',issuebook,name="issuebook"),
    path('issuedbookview',issuedbookview,name="issuedbookview"),
   
]