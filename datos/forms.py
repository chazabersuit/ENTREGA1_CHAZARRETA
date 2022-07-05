
from django import forms


class Formulario_Ingreso(forms.Form):
    interprete=forms.CharField(max_length=30)
    album=forms.CharField(max_length=30)
    año=forms.DateField(required=True)
    link=forms.CharField(max_length=100)
    
class Busqueda(forms.Form):
    interprete=forms.CharField(max_length=30, required=False)