from django import forms

class mi_formulario(forms.Form):
    name = forms.CharField(max_length=20, )
    apellido = forms.CharField(max_length=10)
    descripcion = forms.CharField(max_length=200)

class formulario_create_paquete(forms.Form):
    name = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    price= forms.FloatField()

class formulario_create_vuelo(forms.Form):
    name = forms.CharField(max_length=200)
    departure = forms.CharField(max_length=200)
    destination = forms.CharField(max_length=200)
    date_departue = forms.DateField()
    date_return = forms.DateField()
    price= forms.FloatField()

class formulario_create_hotel(forms.Form):
    name = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
    date_departue = forms.DateField()
    date_return = forms.DateField()
    price = forms.FloatField()