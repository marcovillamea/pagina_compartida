from pyexpat import model
from django.contrib import admin

from viajes.models import Paquete,Vuelo,Hotel

@admin.register(Paquete)
class Products_admin(admin.ModelAdmin):
    list_display = ['name', 'location', 'description', 'price']

@admin.register(Vuelo)
class Products_admin(admin.ModelAdmin):
    list_display = ["name", "departure", "destination", "date_departue" , "date_return" , "price" ]

@admin.register(Hotel)
class Products_admin(admin.ModelAdmin):
    list_display = ["name", "location", "date_departue" , "date_return" , "price" ]