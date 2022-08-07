


from django.shortcuts import render,redirect

from viajes.models import viajes

from viajes.forms import mi_formulario


# def info(request):
#     todo = viajes.objects.create(name = "marco", apellido = "villamea", descripcion = "estoy probando 2.0")
#     context = {
#         "todo": todo
        
#         }

#     return render(request,"informacion.html",context=context)


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


def search_products(request):
    search = request.GET["search"]
    list = viajes.objects.filter(name__icontains=search)
    context = {
        "list":list
    }

    return render(request, "search_products.html",context=context)
