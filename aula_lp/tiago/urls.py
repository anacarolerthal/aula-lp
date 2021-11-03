from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("GM_first", views.GM_first, name="GM_first"),
    path("player_first", views.player_first, name="player_first"),
    path("data/<int:year>/<int:month>", views.data, name="dynamic_date"),
    path("date/<int:year>/<int:month>", views.dynamic_date, name="dynamic_date")
]
