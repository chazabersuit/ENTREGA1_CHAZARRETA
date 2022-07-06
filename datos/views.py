from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import Formulario_Ingreso, Busqueda

from datos.models import Videos

# Create your views here.
def index(request):
    formulario_ingreso=Formulario_Ingreso()
    if request.method == 'POST':
        form= Formulario_Ingreso(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            datos_artista=Videos(interprete=data.get('interprete'),album=data.get('album'),año=data.get('año'), link=data.get('link'))
            datos_artista.save()
            return redirect('busqueda')
        else:
            return render(request,'index.html',{'formulario_ingreso':form})
    return render(request,'index.html',{'formulario_ingreso':formulario_ingreso})


def sobre_nosotros(request):
    return render(request,'sobre_nosotros.html',{})


def busqueda(request):
    formulario_busqueda=Busqueda()
    nombre_de_busqueda= request.GET.get('interprete')
    if nombre_de_busqueda:
         listado_busqueda=Videos.objects.filter(interprete__icontains=nombre_de_busqueda)
         return render(request,'busqueda.html',{'formulario_busqueda':formulario_busqueda,'listado_busqueda':listado_busqueda})
    else:
        listado_busqueda=Videos.objects.all()
    return render(request,'busqueda.html',{'formulario_busqueda':formulario_busqueda,'listado_busqueda':listado_busqueda})

