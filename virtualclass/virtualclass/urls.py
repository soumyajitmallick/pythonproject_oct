"""
URL configuration for virtualclass project.

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
from django.urls import path,include
from Home import views as hviews
from Register import views as rviews
from login import views as lviews

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('faculty/', include('faculty.urls')),
    path('staff/', include('staff.urls')),
    path('student/', include('student.urls')),
    path('myadmin/', include('myadmin.urls')),



    path('admin/', admin.site.urls),            #path("url name",function name)
    #Register
    path('register/',rviews.register, name="register"),

    #home
    path('index',hviews.index,name="index"),
    path('about',hviews.about,name="about"),
    path('',hviews.home,name="home"),
    path('contact',hviews.contact_details,name="contact"),
    path('faqs',hviews.faqs,name="faqs"),
    path('add',hviews.add,name="add"),


    #Login
    path('login/',lviews.login,name="login"),
    path('viewdata',lviews.viewdata,name="viewdata"),
    path('update/',lviews.update,name='update')


    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
