from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import Formulario_Ingreso, Busqueda

from datos.models import Videos

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def cargar(request):
    formulario_ingreso=Formulario_Ingreso()
    if request.method == 'POST':
        form= Formulario_Ingreso(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            datos_artista=Videos(interprete=data.get('interprete'),album=data.get('album'),año=data.get('año'), link=data.get('link'))
            datos_artista.save()
            return redirect('busqueda')
        else:
            return render(request,'cargar.html',{'formulario_ingreso':form})
    return render(request,'cargar.html',{'formulario_ingreso':formulario_ingreso})


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

def editar(request, id):
    dato= Videos.objects.get(id=id)
    if request.method=='POST':
        form=Formulario_Ingreso(request.POST)
        if form.is_valid():
            dato.interprete=form.cleaned_data.get('interprete')
            dato.album=form.cleaned_data.get('album')
            dato.año=form.cleaned_data.get('año')
            dato.link=form.cleaned_data.get('link')
            dato.save()
            return redirect('busqueda')
        else:
            return render(request,'editar.html',{'form':form,'dato':dato})
    
    formulario=Formulario_Ingreso(initial={'interprete':dato.interprete,'album':dato.album,'año':dato.año,'link':dato.link})
    return render(request,'editar.html',{'formulario':formulario,'dato':dato})

def eliminar(request,id):
    dato=Videos.objects.get(id=id)
    dato.delete()
    return redirect('busqueda')
