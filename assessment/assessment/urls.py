"""
URL configuration for assessment project.

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
from assessment1 import views as aviews
from assessment2 import views as a2views
from assessment3.views import leave_apply 

urlpatterns = [
    # FOR ASSESSMENT 1

#     path('admin/', admin.site.urls),                 
#     path("url name",function name)
#     path('home',aviews.home, name="admin"),
#     path('user',aviews.user, name="user"),
#     path('signup',aviews.signup, name="signup"),
#     path('login',aviews.login, name="login"),

    # FOR ASSESSMENT 2
    path('order',a2views.order,name="order"),
    path('orderplace',a2views.orderplace,name="orderplace"),

    # FOR ASSESSMENT 3
    path('leave/', leave_apply ),
    path('admin/',admin.site.urls),
]
