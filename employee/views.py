from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Person


def index(request):
    employee = Person.objects.all().count()
    context = {
    'employee':employee
    }
    return render(request,'base.html',context)

def employee(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']

        obj = Person.objects.create(first_name=first_name,
                            last_name=last_name,
                            email=email)
        if obj:
            return redirect('/employee')
        return HttpResponse("Employee is not created")
    else:
        persons = Person.objects.all()
        context = {
            'persons':persons
        }
    return render(request,'employee/employee.html',context)

@login_required
def employee_update(request,id):
    person = Person.objects.get(id=id)
    if request.method == 'POST':
        person.first_name = request.POST['first_name']
        person.last_name = request.POST['last_name']
        person.email = request.POST['email']
        person.save()
        return redirect('/employee')
    context = {
    'person':person
    }

    return render(request,'employee/employee_update.html',context)


def employee_delete(request,id):
    person = Person.objects.get(id=id)
    if request.method == 'POST':
        person.delete()
        return redirect('/employee')
    context = {
    'person':person
    }

    return render(request,'employee/employee_delete.html',context)


