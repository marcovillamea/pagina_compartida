from django import forms

class mi_formulario(forms.Form):
    name = forms.CharField(max_length=20, )
    apellido = forms.CharField(max_length=10)
    descripcion = forms.CharField(max_length=200)

    