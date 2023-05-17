from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
#from pages.forms import create_user_form
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# login page (home)

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password is Incorrect!')
            return render(request,'index.html', {})

    return render(request,'index.html', {})

    # log out

    # index
def dashboard(request):
    return render(request,'dashboard/dashboard.html', {})