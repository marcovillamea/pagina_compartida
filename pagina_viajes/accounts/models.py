from django.db import models


class User_profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    general_info = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='profile_image/', blank=True)
    
    def __str__(self):
        return self.user.username + ' - profile'