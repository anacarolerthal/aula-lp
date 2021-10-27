from django.urls import path
from bruno import views 

urlpatterns = [
    path("", views.especial, name="especial"),
    path("index/", views.index, name="index"),
]