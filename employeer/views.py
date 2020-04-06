from django.shortcuts import render,redirect

# Create your views here.

from .forms import EmployeerForm
from django.http import HttpResponse

from .models import Employeer

def employeer(request):
    context = {
        'employeers':Employeer.objects.all()
    }
    return render(request,'employeer/employeer.html',context)

def AddEmployeer(request):
    if request.method == 'POST':
        form = EmployeerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/employeer')
    context = {
        'form':EmployeerForm()
    }
    return render(request,'employeer/add_employeer.html',context)

def employeer_update(request,id):
    instance = Employeer.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeerForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/employeer')
    context = {
        'form':EmployeerForm(instance = instance )
    }
    return render(request,'employeer/add_employeer.html',context)