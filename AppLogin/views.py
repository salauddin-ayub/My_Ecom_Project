from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse


# Authentication 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# forms & Model
from AppLogin.models import Profile
from AppLogin.forms import SignUpForm, ProfileForm
# Create your views here.

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        formm = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('AppLogin:login'))
    return render(request, 'AppLogin/sign_up.html', context={'form':form})

def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)   
        if form.is_valid():
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Logged in')
    return render(request, 'AppLogin/login.html', context={'form':form})     

@login_required
def logout_user(request):
    logout(request)
    return HttpResponse("Logged Out")                       

