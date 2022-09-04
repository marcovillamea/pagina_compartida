from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from pagina_viajes.views import index, not_found
from about.views import about_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path("info/",include("viajes.urls")),
    path("", index, name="index"),
    path("accounts/", include("accounts.urls")),
    path("", index, name="index"),
    path("not-found/",not_found, name ="notfound"),
    path("about/", about_us, name ="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
