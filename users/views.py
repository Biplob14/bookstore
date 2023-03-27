from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


# Create your views here.
def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)
            
            if user:
                login(request, user)
                print("redirection to books page")
                return redirect('books:all_books')
    else:
        form = RegistrationForm()

    context = {
        "user_form": form
    }
    return render(request, "signup.html", context)

def login_user(request):
    form = LoginForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                redirect('books.all_books')
            else:
                pass
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    redirect('books.all_books')