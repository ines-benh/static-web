from django import forms 
from order.models import Order

class   OrderModelform(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class   OrderItemModelform(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'