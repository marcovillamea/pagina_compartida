from django.db import models


class viajes(models.Model):
    name = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300)



    def __str__(self):
        return f"nombre: {self.name} - apellido: {self.apellido} - descripcion: {self.descripcion}"







