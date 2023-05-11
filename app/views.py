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
        form = Register(request.POST)
        # check whether it is valid:
        if form.is_valid():
            
            # redirect to a new URL:
            return HttpResponseRedirect("/registered successfully/")
    else:
        return render(request, "register.html", {"form":form})

def dashboard(request):
    return render(request, 'templates/dashboard.html', {})

def create_blog(request):
    return render(request, 'blog/create_blog.html', {})

def read_blog(request):
    return render(request, 'blog/read_blog.html', {})

def admin_blog(request):
    return render(request, 'blog/admin_blog.html', {})

def delete_blog(request):
    return render(request, 'blog/delete_blog.html', {})

def create_Comment(request):
    return render(request, 'Comment/create_Comment.html', {})

def read_Comments(request):
    return render(request, 'Comment/read_Comment.html', {})

def admin_Comment(request):
    return render(request, 'Comment/Comment.html', {})

def delete_Comment(request):
    return render(request, 'Comment/delete_Comment.html', {})

def create_User(request):
    return render(request, 'User/create_User.html', {})

def read_Users(request):
    return render(request, 'User/read_User.html', {})

def admin_User(request):
    return render(request, 'User/User.html', {})

def delete_User(request):
    return render(request, 'User/delete_User.html', {})