from django import forms 
from .models import Category , Product

class CategoryModelform(forms.ModelForm):
    class meta:
        model = Category
        fields = ['name']

class ProductModelForm(forms.ModelForm):
    class Meta:

        model = Product
        fields = '__all__'


