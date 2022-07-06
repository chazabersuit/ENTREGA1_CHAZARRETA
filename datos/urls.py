from django import views
from django.urls import path
from .views import busqueda, index, sobre_nosotros


urlpatterns = [
    path('',index ,name='index'),
    path('busqueda/',busqueda, name='busqueda'),
    path('sobre_nosotros/',sobre_nosotros, name='sobre_nosotros'),
]