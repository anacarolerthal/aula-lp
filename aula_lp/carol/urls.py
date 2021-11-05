from django.urls import path
from carol import views 

urlpatterns = [
    path("", views.index, name="ferias1"),
    path("ferias2/", views.ferias2, name="ferias2"),
    path("ferias3/", views.ferias3, name="ferias3"),
    path("ferias/", views.redirect_ferias, name="ferias1"),
    path("date/<int:month>", views.by_month, name="by_month"),
]
