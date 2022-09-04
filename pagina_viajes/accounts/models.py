from django.db import models


class User_profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    nombre = models.CharField(max_length=200, blank=True)
    apellido = models.CharField(max_length=200, blank=True)
    celular = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='profile_image/', blank=True)

    def __str__(self):
        return self.user.username + " - profile"