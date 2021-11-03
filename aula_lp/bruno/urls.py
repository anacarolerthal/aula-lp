from django.urls import path
from bruno import views 

urlpatterns = [
    path("", views.especial, name="especial"),
    path("index/", views.index, name="index"),
    path("pagina2/", views.pagina2, name="pagina2"),
    path("pagina3/", views.pagina3, name="pagina3"),
]