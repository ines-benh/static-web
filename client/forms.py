from django import forms 
from Client.models import client

class ClientModelform(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
                 'full_name',
                 'family_name',
                 'email',
                 'number',
                 ]