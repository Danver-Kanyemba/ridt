from django.shortcuts import render

# Create your views here.

def index(request):
    login=False;
    return render(request, "index.html",{"login":login})