from django.urls import path
from myadmin.views import ahome,aupdate,dashboad,profile,viewprofile


urlpatterns=[
    path('ahome',ahome,name="ahome"),
    path('aupdate/',aupdate,name="aupdate"),
    path('dashboad',dashboad,name="dashboad"),
    path('profile',profile,name="profile"),
    path('viewprofile',viewprofile,name="viewprofile"),
]