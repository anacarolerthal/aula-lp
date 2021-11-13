from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    lista_rpgs = ["Pathfinder", "Dungeons and Dragons", "Call of Cthulu", "Dread", "Mutants and Masterminds"]
    context = {
        "lista_rpgs": lista_rpgs
    }
    return render(request, 'index.html', context)


def GM_first(request):
    return render(request, 'GM_first.html')


def player_first(request):
    return render(request, 'player_first.html')


def dynamic_date(request, year, month):
    if month < 0 or month > 12:
        return HttpResponseNotFound("Página não existe!")
    return render(request, 'index.html')


def data(request, year, month):
    redirect_url = reverse("dynamic_date", args=[year, month])
    return HttpResponseRedirect(redirect_url)


def rpg(request, sistema):
    context = {
        "sistema": sistema
    }
    return render(request, "rpg.html", context)