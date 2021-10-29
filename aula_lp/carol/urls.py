from django.urls import path
from carol import views 

urlpatterns = [
    path("special/", views.special, name="special"),
    path("index/", views.index, name="index"),
]
