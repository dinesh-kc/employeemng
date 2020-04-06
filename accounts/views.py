from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required


from .forms import LoginForm,ProfileForm

# Create your views here.
def RegisterUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(username=data['username']
                                       )
            user.set_password(data['password1'])

            user.save()

            return redirect('/')
    form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'register.html',context)


def LoginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('/')
    form = LoginForm()
    context = {
        'form':form
    }
    return render(request,'login.html',context)

def LogoutUser(request):
    #logout user 
    logout(request)
    return redirect('/login')

@login_required
def UserProfile(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        
        user_obj = User.objects.get(id=request.user.id)
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.save()
        return redirect('/profile')
        
    form = ProfileForm(initial=
                       {
                        'first_name':request.user.first_name,
                        'last_name':request.user.last_name
                       
                       },
                       )
    context = {
        'form':form
    }
    return render(request,'profile.html',context)