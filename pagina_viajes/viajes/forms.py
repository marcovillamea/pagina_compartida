from django import forms


class formulario_create_paquete(forms.Form):
    name = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    price= forms.FloatField()
    image= forms.ImageField(required=False)

class formulario_create_vuelo(forms.Form):
    name = forms.CharField(max_length=200)
    departure = forms.CharField(max_length=200)
    destination = forms.CharField(max_length=200)
    date_departue = forms.CharField(max_length=200)
    date_return = forms.CharField(max_length=200)
    price= forms.FloatField()
    image= forms.ImageField(required=False)

class formulario_create_hotel(forms.Form):
    name = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
    date_departue = forms.CharField(max_length=200)
    date_return = forms.CharField(max_length=200)
    price = forms.FloatField()
    image= forms.ImageField(required=False)