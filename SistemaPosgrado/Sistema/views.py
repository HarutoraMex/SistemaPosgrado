from django.http.request import HttpHeaders, HttpRequest
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
#Metodo de vizualización de Login
def Login (request):
    return render(request,"Login.html")
#Metodo de vizualización de Login
def Formatos (request):
    return render(request,"Formatos.html")