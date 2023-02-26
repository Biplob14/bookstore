from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


# Create your views here.
def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        print("form data submitted")
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
    else:
        form = RegistrationForm()

    context = {
        "user_form": form
    }
    return render(request, "signup.html", context)

def login_user(request):
    print(request)
    return HttpResponse('login page')