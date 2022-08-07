from cmath import inf
from django.urls import path

from viajes.views import viajeformulario, lista_viajes, search_products


urlpatterns = [
    path("formulario/", viajeformulario, name= "formulario"),
    path("lista_viajes/", lista_viajes, name= "lista" ),
    path("search_products/",search_products, name = "search products")
    

]

