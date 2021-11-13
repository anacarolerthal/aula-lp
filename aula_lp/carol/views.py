from django.http.response import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

def index(request):
    esportes = ["skate park","vôlei de quadra","polo aquático","canoagem slalom"]
    context = {
        "pessoa":"Tiago",
        "esportes": esportes, 

    }
    return render(request, "ferias1.html", context)

def ferias2(request):
    return render(request, "ferias2.html")

def ferias3(request):
    return render(request, "ferias3.html")

def feriasbasic(request):
    return render(request, "ferias-dtl.html")

def redirect_ferias(request):
    redirect_url = reverse("ferias1")
    return HttpResponseRedirect(redirect_url)

def by_month(request, month):
    if month < 0 or month > 12:
        raise Http404()
    elif month < 6:
        return render(request, 'ferias2.html')
    elif month < 8: 
        return render(request, 'ferias1.html')
    elif month < 10:
        return render(request, 'ferias2.html')
    else: 
        return render(request, 'ferias3.html')

