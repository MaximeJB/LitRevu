from django.shortcuts               import render, redirect
from django.contrib.auth            import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms      import AuthenticationForm
from .forms                         import CustomUserCreationForm

User = get_user_model()


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("Review:feed")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    login_form = AuthenticationForm()
    register_form = CustomUserCreationForm()

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "login":
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                login(request, login_form.get_user())
                return redirect("Review:feed")
        elif action == "register":
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect("Review:feed")

    return render(
        request,
        "users/login.html",
        {"login_form": login_form, "register_form": register_form},
    )


@login_required
def logout_view(request):
    if request.method in ("GET", "POST"):
        logout(request)
        return redirect('Review:feed')
