from django.db import models

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'


class Product (models.Model):
    name = models.CharField(max_length=255)
    buyingPrice = models.FloatField(blank=True,null=True)
    sellingPrice= models.FloatField(blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)

    Category =models.ForeignKey("product.Category",on_delete =models.SET_NULL,null=True)

    def __str__(self):
        return self.name 

    class Meta:
        unique_together = ['name', 'description']
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'
      