from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    website_url = models.URLField(max_length=255)
    def __str__(self):
        return self.name
    
