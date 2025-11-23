# from django.http import HttpResponse
from django.shortcuts import redirect


def homepage(request):
    if request.user.is_authenticated:
        return redirect("Review:feed")
    return redirect("UserCustom:user-login")
