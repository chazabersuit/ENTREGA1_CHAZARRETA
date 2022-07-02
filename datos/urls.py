from django import views
from django.urls import path
from .views import index, sobre_nosotros


urlpatterns = [
    path('',index ,name='index'),
    path('sobre_nosotros/',sobre_nosotros, name='sobre_nosotros')
]