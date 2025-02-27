from django import forms
from .models import Item

class ItemForms(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','description','price','image']
        