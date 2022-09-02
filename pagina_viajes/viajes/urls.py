from cmath import inf
from django.urls import path
from viajes.views import verPaquetes, verHotel, verVuelo, formulario_paquete,formulario_vuelo,formulario_hotel
from viajes.views import search_hotel, viajeformulario, lista_viajes, search_vuelo, search_paquete
from viajes.views import delete_hotel, delete_paquete, delete_vuelo
from viajes.views import update_hotel, update_vuelo, update_paquete


urlpatterns = [
    path("formulario/", viajeformulario, name= "formulario"),
    path("lista_viajes/", lista_viajes, name= "lista" ),
    path("search_products/",search_hotel, name = "search hotel"),
    path("search_products/",search_vuelo, name = "search vuelo"),
    path("search_products/",search_paquete, name = "search paquete"),
    path("viajes-paquetes/",verPaquetes),
    path("viajes-hotels/",verHotel),
    path("viajes-vuelos/",verVuelo),
    path("create-paquete/", formulario_paquete),
    path("create-vuelo/", formulario_vuelo),
    path("create-hotel/", formulario_hotel),
    path("delete-hotel/<int:pk>/", delete_hotel, name = "delete-hotel"),
    path("delete-vuelo/<int:pk>/", delete_vuelo, name = "delete-vuelo"),
    path("delete-paquete/<int:pk>/", delete_paquete, name = "delete-paquete"),
    path("update-hotel/<int:pk>/", update_hotel, name ="update_hotel"),
    path("update-vuelo/<int:pk>/", update_vuelo, name ="update_vuelo"),
    path("update-paquete/<int:pk>/", update_paquete, name ="update_paquete"),
]
