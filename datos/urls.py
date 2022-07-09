from django import views
from django.urls import path
from .views import busqueda, index, sobre_nosotros, editar, eliminar,cargar


urlpatterns = [
    path('',index ,name='index'),
    path('cargar/',cargar, name='cargar'),
    path('busqueda/',busqueda, name='busqueda'),
    path('sobre_nosotros/',sobre_nosotros, name='sobre_nosotros'),
    path('editar/<int:id>/',editar, name='editar'),
    path('eliminar/<int:id>/',eliminar, name='eliminar'),
]
