from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from pages.forms import UserLoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    context = {}
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('dashboard')
        else:
            redirect('loginpage')
            form = UserLoginForm()
            context['form'] = form
    else:
        form = UserLoginForm()
        context['form'] = form
    return render(request,'login.html', context)

def register_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request,user)
            return redirect('loginpage')
        else:
            form = UserCreationForm()
            context['form'] = form
            return redirect('register')
    else:
        form = UserCreationForm()
        context['form'] = form
    return render(request,'register.html', context)




@login_required(login_url = 'loginpage')
def dashboard(request):
    return render(request,'dashboard.html',{})


def user_logout(request):
    logout(request)
    return redirect('loginpage')


    