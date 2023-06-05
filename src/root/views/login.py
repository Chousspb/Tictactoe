from django.contrib.auth import login as auth_login, authenticate
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


def login(request: HttpRequest):
    if request.method == "POST":
        user_name = request.POST['username']
        password = request.POST['password']
        user = request.user
        if not user.is_authenticated:
            user = authenticate(username=user_name, password=password)
            if user is not None:
                auth_login(request, user)
        return redirect("main")

    if not request.user.is_authenticated:
        return render(request, "login.html")

    else:
        return redirect("main")