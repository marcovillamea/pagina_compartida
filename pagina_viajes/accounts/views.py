from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout , authenticate
from accounts.forms import User_registration_form
from accounts.models import User_profile
from django.contrib.auth.decorators import login_required
from accounts.forms import User_registration_form

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {'message':f'Bienvenido { username }'}
                return render(request, 'index.html', context = context)
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'error': 'El usuario y/o contraseña no son correctas. Inténtelo de nuevo.', 'form': form})
    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'accounts/login.html', context)
    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'accounts/register.html', {'form': form})

def show_profile(request):
    return render(request, 'accounts/profile.html', {"user": user})

def edit_profile(request):
    if request.method == 'POST':
        post_data = request.POST
        aux = {
            "password1": post_data['password1'],
            "password2": post_data.get('password2'),
            "username": post_data.get('username'),
            "description": post_data.get('description'),
            "webpage": post_data.get('webpage'),
        }
        user.update(aux)
        return redirect(show_profile)
    if request.method=="GET":
        miFormulario = User_registration_form(initial=user)
        return render(request, "accounts/editprofile.html", {"miFormulario": miFormulario, "user": user}) 

def miFormulario(request):
    return render(request, "")

user = {
    "username": "Ingrese su usuario",
    "location": "Coderhouse",
    "description": "Ingrese su descripción",
    "webpage": "Ingrese link de sus redes sociales",
    "email": "No puede modificar su dirección de mail",
    "_meta": "a",
    "password1": "Edite su contraseña",
    "password2": "Edite su contraseña nuevamente",
    "image": "https://us.123rf.com/450wm/koblizeek/koblizeek2001/koblizeek200100050/138262629-usuario-miembro-de-perfil-de-icono-de-hombre-vector-de-s%C3%ADmbolo-perconal-sobre-fondo-blanco-aislado-.jpg?ver=6"
}