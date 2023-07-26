from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):     
    email = models.CharField(max_length=200)
    avatar = models.ImageField(blank=True)
    phone_number = models.CharField(max_length=20,blank=True)
    address = models.CharField(max_length=500,blank=True)

    def __str__(self) -> str:
        return self.username


