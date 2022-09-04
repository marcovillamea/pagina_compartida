from django.db import models


class Paquete(models.Model):
    name = models.CharField(max_length=200)
    location = models.TextField()
    description = models.TextField()
    price= models.FloatField()
    image=models.ImageField(upload_to="viajes/",null=True, blank=True)

    def __str__(self):
        return self.name

class Vuelo(models.Model):
    name = models.CharField(max_length=200)
    departure = models.TextField()
    destination = models.TextField()
    date_departue = models.DateField(auto_now_add=True, null=True, blank=True)
    date_return = models.DateField(auto_now_add=True, null=True, blank=True)
    price= models.FloatField()
    image=models.ImageField(upload_to="viajes/",null=True, blank=True)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    location= models.TextField()
    date_departue = models.DateField(auto_now_add=True, null=True, blank=True)
    date_return = models.DateField(auto_now_add=True, null=True, blank=True)
    price= models.FloatField()
    image=models.ImageField(upload_to="viajes/",null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hoteles"
