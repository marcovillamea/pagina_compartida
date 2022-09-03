
from django.contrib import admin
from django.urls import path,include
from pagina_viajes.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("info/",include("viajes.urls")),
    path("", index, name="index"),
    path("accounts/", include("accounts.urls")),
]
