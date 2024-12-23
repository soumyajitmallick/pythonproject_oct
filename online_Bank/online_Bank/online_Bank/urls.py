"""
URL configuration for online_Bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from signup.views import signup,contact,index
from login.views import login
from user.views import userhome,deposite_withdraw,balance_details,current_balance

urlpatterns = [
    path('admin/', admin.site.urls),

    #USER
    path('userhome',userhome,name="userhome"),
    path('deposite_withdraw',deposite_withdraw,name="deposite_withdraw"),
    path('balance',balance_details ,name="balance"),
    path('current_balance',current_balance ,name="current_balance"),

    #LOGIN
    path('login',login ,name="login"),

    #SIGNUP
    path('signup',signup,name='signup'),
    path('index',index,name='index'), 
    path('contact',contact,name='contact'),

]