from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

def redireciona(request, param):
    url_redireciona = reverse("view-dinamica-int", args=[param])
    return HttpResponseRedirect(url_redireciona)

def index(request):
    return HttpResponse("<strong>Bruno :)</strong>")

def especial(request):
    return render(request, "bruno.html")

def pagina2(request):
    return render(request, "bruno2.html")

def pagina3(request):
    return render(request, "bruno3.html")

def dinamica(request,param):
    if param == 1:
        return HttpResponse("<h1>Parâmetro 1</p>")
    if param == 2:
        return HttpResponse("<h1>Parâmetro 2</p>")
    if param == 42:
        return HttpResponse("<h1>Parâmetro 42</p>")
    else:
        raise Http404()
        # return HttpResponseNotFound("<h1> Página não encontrada... :/</h1>")

def pagina_dinamica(request):
    from datetime import date, datetime
    data = date.today()
    hora = datetime.now().strftime('%H:%M:%S')
    data_hora = [data, hora]
    contexto = {
        #"data": data,
        #"hora": hora,
        "data_hora": data_hora,
        "nome": "Bruno",
        "sobrenome": "Fornaro"
    }
    return render(request, "pagina_dinamica_dtl.html", contexto)
