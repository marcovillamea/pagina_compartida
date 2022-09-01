from django.shortcuts import render,redirect
from multiprocessing import context
from datetime import date
from django.http import HttpResponse

from viajes.models import Paquete, Vuelo, Hotel

from viajes.models import viajes

from viajes.forms import mi_formulario, formulario_create_paquete,formulario_create_vuelo,formulario_create_hotel


def viajeformulario(request):
    if request.method == "POST":
        viajeformulario = mi_formulario(request.POST)

        if viajeformulario.is_valid():
            viajes.objects.create(
                name = viajeformulario.cleaned_data["name"],
                apellido = viajeformulario.cleaned_data["apellido"],
                descripcion = viajeformulario.cleaned_data["descripcion"],
                )

            return redirect(lista_viajes)
            
        

    elif request.method == "GET":
        viajeformulario = mi_formulario()
        context = {
            "viajeformulario": viajeformulario
        }
     
        return render(request,"viajeformulario.html",context=context)


def lista_viajes(request):
    list = viajes.objects.all()
    context = {
        "list": list
    }

    return render(request,"lista_de_lugares.html",context=context)


def verPaquetes(request):
    paquetes = Paquete.objects.all()
    return render(request,"paquete.html",context={"paquetes" : paquetes})

def verVuelo(request):
    vuelos = Vuelo.objects.all()
    return render(request,"vuelo.html",context={"vuelos" : vuelos})

def verHotel(request):
    hotels = Hotel.objects.all()
    return render(request,"hotel.html",context={"hotels" : hotels})

def formulario_paquete(request):
    if request.method == "POST":
        form = formulario_create_paquete(request.POST)

        if form.is_valid():
            Paquete.objects.create(
                name = form.cleaned_data["name"],
                location = form.cleaned_data["location"],
                description = form.cleaned_data["description"],
                price= form.cleaned_data["price"]
                )
            return redirect(verPaquetes)

    elif request.method == "GET":
        form = formulario_create_paquete()
        context = {"form":form}
        return render(request,"formulario_nuevopaquete.html", context=context)

def formulario_vuelo(request):
    if request.method == "POST":
        form = formulario_create_vuelo(request.POST)
        
        if form.is_valid():
            Vuelo.objects.create(
                name = form.cleaned_data["name"],
                departure = form.cleaned_data["departure"],
                destination = form.cleaned_data["destination"],
                date_departue = form.cleaned_data["date_departue"],
                date_return = form.cleaned_data["date_return"],
                price= form.cleaned_data["price"]
                )
        return redirect(verVuelo)
    elif request.method == "GET":
        form = formulario_create_vuelo()
        context = {"form": form}
        return render(request,"formulario_nuevovuelo.html", context = context)

def formulario_hotel(request):
    if request.method == "POST":
        form = formulario_create_hotel(request.POST)

        if form.is_valid():
            Hotel.objects.create(
                name = form.cleaned_data["name"],
                location = form.cleaned_data["location"],
                date_departue = form.cleaned_data["date_departue"],
                date_return = form.cleaned_data["date_return"],
                price= form.cleaned_data["price"]
                )
        return redirect(verHotel)
    elif request.method == "GET":
        form = formulario_create_hotel()
        context = {"form": form}
        return render(request,"formulario_nuevohotel.html", context = context)

def search_hotel(request):
    print(request.GET)
    hotel = Hotel.objects.filter(name__icontains = request.GET['search'])
    context = {'hotel':hotel}
    return render(request, 'search_products.html', context= context)

def search_vuelo(request):
    print(request.GET)
    vuelo = Vuelo.objects.filter(name__icontains = request.GET['search'])
    context = {'vuelo':vuelo}
    return render(request, 'search_products.html', context= context)

def search_paquete(request):
    print(request.GET)
    paquete = Paquete.objects.filter(name__icontains = request.GET['search'])
    context = {'paquete':paquete}
    return render(request, 'search_products.html', context= context)

def delete_hotel(request, pk):
    if request.method == "GET":
        hotel = Hotel.objects.get(pk=pk)
        context = {'hotel':hotel}
        return render(request, "delete_hotel.html", context = context)
    elif request.method == "POST":
        hotel = Hotel.objects.get(pk=pk)
        hotel.delete()
        return redirect(verHotel)