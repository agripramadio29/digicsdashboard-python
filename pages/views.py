from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pages.models import displayUserName
from django.contrib.auth.models import User

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
def log_out(request):
    logout(request)
    return redirect('home')

    # index
@login_required(login_url='home')    
def dashboard(request):
    return render(request,'dashboard/dashboard.html', {})

    # user
@login_required(login_url='home')
def user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    # display data
    displaynames = User.objects.all()


    context = {'form': form, "displayUserName": displaynames}
    return render(request, 'master/user.html', context)