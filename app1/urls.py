from django.contrib import admin
from django.urls import path
from . import views

#Quiero que cuando escriba '' en el url, se ejecute lo que está en ruta.funcion
urlpatterns = [
    path('v1/', views.vista1),
]