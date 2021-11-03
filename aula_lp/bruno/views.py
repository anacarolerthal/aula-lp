from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<strong>Bruno :)</strong>")

def especial(request):
    return render(request, "bruno.html")

def pagina2(request):
    return render(request, "bruno2.html")

def pagina3(request):
    return render(request, "bruno3.html")