from django.http import HttpResponse
from django.shortcuts import render

from datos.models import Videos

# Create your views here.
def index(request):
    
    dato=Videos(interprete="Ibiza Pareo",album="Ibiza Pareo",año=2019)
    dato1=Videos(interprete="Bersuit Vergarabat",album="De la cabeza",año=2002)

    
    return render(request,'index.html',{'lista_artistas':[dato, dato1]})

def sobre_nosotros(request):
    return render(request,'sobre_nosotros.html',{})