from django import forms 
from contact.models import Contact

class ContactModelform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
                 'name',
                 'title',
                 'email',
                 'description',
                 ]