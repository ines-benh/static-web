from django.db import models
from client.models import Client
from product.models import Product


class  Order (models.Model):
    
    id = models.UUIDField(primary_key=True , default = uuid.uuid4, editable=False)
    TotalPrice = models.DecimalField()
    client = models.ForeignKey(order.Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.TotalPrice}'


class OrderItem(models.Model):
    Product = models.ForeignKey(orderitem.Product, on_delete=models.CASCADE)