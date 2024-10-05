from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from login.templates.forms.forms import signup_user_form
# from templates.forms.forms  import UserCreationForm

# Create your views here.

def login_user(request): #----- this is for logging in --
    if request.method == "POST":    
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, ("Invalid username/password!"))
            return redirect('login_user')
    else:
        return render(request, 'authentication/login.html', {})



def logout_user(request): #-- this code is logging out
    logout(request)
    messages.success(request, ("You were logout!!"))
    return redirect('login_user')


def signup_user(request):
    if request.method == "POST":
        form = signup_user_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('login_user')
    else:
        form = signup_user_form()
    return render(request, 'authentication/signup.html', {'form':form})

def user_name(request):
    users = ""
    return HttpResponse(users)