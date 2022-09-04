from django.shortcuts import render,redirect
from multiprocessing import context
from datetime import date
from django.http import HttpResponse
from viajes.models import Paquete, Vuelo, Hotel
from viajes.forms import formulario_create_paquete,formulario_create_vuelo,formulario_create_hotel


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
        form = formulario_create_paquete(request.POST, request.FILES)

        if form.is_valid():
            Paquete.objects.create(
                name = form.cleaned_data["name"],
                location = form.cleaned_data["location"],
                description = form.cleaned_data["description"],
                price= form.cleaned_data["price"],
                image=form.cleaned_data["image"]
                )
            return redirect(verPaquetes)

    elif request.method == "GET":
        form = formulario_create_paquete()
        context = {"form":form}
        return render(request,"formulario_nuevopaquete.html", context=context)

def formulario_vuelo(request):
    if request.method == "POST":
        form = formulario_create_vuelo(request.POST, request.FILES)
        
        if form.is_valid():
            Vuelo.objects.create(
                name = form.cleaned_data["name"],
                departure = form.cleaned_data["departure"],
                destination = form.cleaned_data["destination"],
                date_departue = form.cleaned_data["date_departue"],
                date_return = form.cleaned_data["date_return"],
                price= form.cleaned_data["price"],
                image=form.cleaned_data["image"]
                )
        return redirect(verVuelo)
    elif request.method == "GET":
        form = formulario_create_vuelo()
        context = {"form": form}
        return render(request,"formulario_nuevovuelo.html", context = context)

def formulario_hotel(request):
    if request.method == "POST":
        form = formulario_create_hotel(request.POST, request.FILES)

        if form.is_valid():
            Hotel.objects.create(
                name = form.cleaned_data["name"],
                location = form.cleaned_data["location"],
                date_departue = form.cleaned_data["date_departue"],
                date_return = form.cleaned_data["date_return"],
                price= form.cleaned_data["price"],
                image=form.cleaned_data["image"]
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

def delete_hotel(request, pk):
    if request.method == "GET":
        hotel = Hotel.objects.get(pk=pk)
        context = {'hotel':hotel}
        return render(request, "delete_hotel.html", context = context)
    elif request.method == "POST":
        hotel = Hotel.objects.get(pk=pk)
        hotel.delete()
        return redirect(verHotel)

def delete_vuelo(request, pk):
    if request.method == "GET":
        vuelo = Vuelo.objects.get(pk=pk)
        context = {'vuelo':vuelo}
        return render(request, "delete_vuelo.html", context = context)
    elif request.method == "POST":
        vuelo = Vuelo.objects.get(pk=pk)
        vuelo.delete()
        return redirect(verVuelo)

def delete_paquete(request, pk):
    if request.method == "GET":
        paquete = Paquete.objects.get(pk=pk)
        context = {'paquete':paquete}
        return render(request, "delete_paquete.html", context = context)
    elif request.method == "POST":
        paquete = Paquete.objects.get(pk=pk)
        paquete.delete()
        return redirect(verPaquetes)

def update_hotel(request, pk):
    if request.method == "POST":
        form = formulario_create_hotel(request.POST)
        if form.is_valid():
            hotel = Hotel.objects.get(id=pk)
            hotel.name = form.cleaned_data["name"]
            hotel.location = form.cleaned_data["location"]
            hotel.date_departue = form.cleaned_data["date_departue"]
            hotel.date_return = form.cleaned_data["date_return"]
            hotel.price= form.cleaned_data["price"]
            hotel.save()
            return redirect(verHotel)
    elif request.method == "GET":
        hotel = Hotel.objects.get(id=pk)
        form = formulario_create_hotel(initial={"Hotel":hotel.name, "Lugar":hotel.location,"Fecha de Entrada":hotel.date_departue,"Fecha de Salida":hotel.date_return,"Precio":hotel.price})
        context = {'form':form}
        return render(request,"update_hotel.html",context)

def update_paquete(request, pk):
    if request.method == "POST":
        form = formulario_create_paquete(request.POST)
        if form.is_valid():
            paquete = Paquete.objects.get(id=pk)
            paquete.name = form.cleaned_data["name"]
            paquete.location = form.cleaned_data["location"]
            paquete.description = form.cleaned_data["description"]
            paquete.price= form.cleaned_data["price"]
            paquete.save()
            return redirect(verPaquetes)
    elif request.method == "GET":
        paquete = Paquete.objects.get(id=pk)
        form = formulario_create_paquete(initial={"Paquete":paquete.name, "Lugar":paquete.location,"Descripcion":paquete.description,"Precio":paquete.price})
        context = {'form':form}
        return render(request,"update_paquete.html",context)

def update_vuelo(request, pk):
    if request.method == "POST":
        form = formulario_create_vuelo(request.POST)
        if form.is_valid():
            vuelo = Vuelo.objects.get(id=pk)
            vuelo.name = form.cleaned_data["name"]
            vuelo.departure = form.cleaned_data["departure"]
            vuelo.destination = form.cleaned_data["destination"]
            vuelo.date_departue = form.cleaned_data["date_departue"]
            vuelo.date_return = form.cleaned_data["date_return"]
            vuelo.price= form.cleaned_data["price"]
            vuelo.save()
            return redirect(verVuelo)
    elif request.method == "GET":
        vuelo = Vuelo.objects.get(id=pk)
        form = formulario_create_vuelo(initial={"Vuelo a ":vuelo.name, "Fecha de Ida":vuelo.date_departue,"Fecha de Vuelta":vuelo.date_return,"Precio":vuelo.price})
        context = {'form':form}
        return render(request,"update_vuelo.html",context)

