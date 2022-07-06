
from django import forms


class Formulario_Ingreso(forms.Form):
    interprete=forms.CharField(max_length=30)
    album=forms.CharField(max_length=30)
    año=forms.DateField(required=False)
    link=forms.CharField(max_length=100,required=False)
    
class Busqueda(forms.Form):
    interprete=forms.CharField(max_length=30, required=True)