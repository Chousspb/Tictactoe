from django.http import HttpRequest
from django.shortcuts import render, redirect
from root.forms.Register import NewUserForm



from django.contrib.auth import login
from django.contrib import messages




def register(request: HttpRequest):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="root/templates/registration/register.html", context={"register_form": form})