from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<strong>nao deu tempooooooooooo</strong>")

def special(request):
    return render(request, "ferias.html")