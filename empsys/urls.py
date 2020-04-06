"""empsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.http import HttpResponse

from employee.views import employee,index,employee_update,employee_delete

from employeer.views import employeer,AddEmployeer,employeer_update

from django.shortcuts import render,redirect

from accounts.views import *

def administrator(request):
    return render(request,'admin_index.html')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('administrator/', administrator),
    path('employee',employee),
    path('employeer',employeer),
     path('add_employeeer',AddEmployeer),
    path('employee_update/<int:id>',employee_update),
    path('employeer_update/<int:id>',employeer_update),
    path('employee_delete/<int:id>',employee_delete),

    path('register',RegisterUser),
    path('login',LoginUser),
    path('logout',LogoutUser),
    path('profile',UserProfile),
    
 
]
