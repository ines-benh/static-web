from django.db import models

# Create your models here.
class Client (models.Model):

    full_name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    email  = models.EmailField(blank=True,null=True)
    number = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.name 