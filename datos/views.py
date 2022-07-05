from django.http import HttpResponse
from django.shortcuts import render
from .forms import Formulario_Ingreso, Busqueda

from datos.models import Videos

# Create your views here.
def index(request):
    listado=Videos.objects.all()
    formulario_ingreso=Formulario_Ingreso()
    formulario_busqueda=Busqueda()
    
    if request.method == 'POST':
        form= Formulario_Ingreso(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            datos_artista=Videos(interprete=data.get('interprete'),album=data.get('album'),año=data.get('año'), link=data.get('link'))
            datos_artista.save()       
            listado=Videos.objects.all()  
            return render(request,'index.html',{'listado':listado,'formulario_ingreso':formulario_ingreso,'formulario_busqueda':formulario_busqueda})
        else:
            return render(request,'index.html',{'formulario_ingreso':form,'listado':listado,'formulario_busqueda':formulario_busqueda})
    
    nombre_de_busqueda= request.GET.get('interprete')
    
    if nombre_de_busqueda:
        listado_busqueda=Videos.objects.filter(interprete__icontains=nombre_de_busqueda) 
        return render(request,'index.html',{'formulario_ingreso':formulario_ingreso,'listado':listado,'listado_busqueda':listado_busqueda,'formulario_busqueda':formulario_busqueda})

    return render(request,'index.html',{'formulario_ingreso':formulario_ingreso,'listado':listado,'formulario_busqueda':formulario_busqueda})

def sobre_nosotros(request):
    return render(request,'sobre_nosotros.html',{})

