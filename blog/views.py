from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(request):
    return HttpResponse("<h1>hola amigo bienvenido pagina de inicio </h1>")


def hoja1(request):
    return HttpResponse("<h2> pagina 2 </h2> ")



    
    
    
