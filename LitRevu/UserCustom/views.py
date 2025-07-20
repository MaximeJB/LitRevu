from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from LitRevu.views import homepage
from .forms import CustomUserCreationForm
from django.http import HttpResponseNotAllowed

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect(homepage)
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", { "form" : form })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(homepage)
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form" : form })

def logout_view(request):
    if request.method in ("GET", "POST"):
        logout(request)
        return redirect(homepage)
    
def logout_confirm(request):
    return render(request, 'logout_confirm.html')


