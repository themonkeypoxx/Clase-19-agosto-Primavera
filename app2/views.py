from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista1(request):
    return HttpResponse("<h1> Hola Django 2 </h1> "
    "<p style= 'color:blue'> Test 1 </p>")

def vista2(request):
    return HttpResponse("<h1> Vista 2 Test app2 </h1>")
