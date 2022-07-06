from django import forms

class FormUsuarios(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False)
    ocupacion = forms.CharField(max_length=30)
    
class BusquedaUsuario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)