from django import forms
from .models import AddProduct  

class AddProductForm(forms.ModelForm):
    class Meta:
        model = AddProduct
        fields = '__all__'  