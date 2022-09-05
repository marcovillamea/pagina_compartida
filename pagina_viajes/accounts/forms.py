from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms

class User_registration_form(UserCreationForm):
    email = forms.EmailField(required=True, label = 'Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            "username":"Nombre de usuario",
            "email":"Correo electrónico",
            "password1": "Contraseña",
            "password2":"Repetir contraseña"
        }
        help_texts = {k:'' for k in fields}

