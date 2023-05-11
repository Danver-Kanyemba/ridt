from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import Login, Register

# Create your views here.
def Login(request):
    form = Login()
    return render(request, "login.html", {"form":form})

def Logout():
    return HttpResponseRedirect("/thanks logout/")

def Register(request):
    form = Register()
    if request.method == "POST":
        form = NameForm(request.POST)
        # check whether it is valid:
        if form.is_valid():
            
            # redirect to a new URL:
            return HttpResponseRedirect("/registered successfully/")
    else:
        return render(request, "register.html", {"form":form})

