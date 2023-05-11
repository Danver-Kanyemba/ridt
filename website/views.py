from django.shortcuts import render

# Create your views here.

def index(request):
    login=False;
    return render(request, "templates/index.html",{"login":login})