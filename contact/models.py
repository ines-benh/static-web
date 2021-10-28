from django.db import models

# Create your models here.
class Contact (models.Model):

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    email  = models.EmailField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name 
        