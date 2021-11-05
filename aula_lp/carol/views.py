from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("ferias1.html")

def ferias2(request):
    return render(request, "ferias2.html")

def ferias3(request):
    return render(request, "ferias3.html")

def redirect_ferias(request):
    redirect_url = reverse("index")
    return HttpResponseRedirect(redirect_url)

def by_month(request, month):
    if month < 0 or month > 12:
        return HttpResponseNotFound("Página não existe!")
    elif month < 6:
        return render(request, 'ferias2.html')
    elif month < 8: 
        return render(request, 'ferias1.html')
    elif month < 10:
        return render(request, 'ferias2.html')
    else: 
        return render(request, 'ferias3.html')

