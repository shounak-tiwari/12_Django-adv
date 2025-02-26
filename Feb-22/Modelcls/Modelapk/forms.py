from django import forms
from .models import AddProduct  # Import your model

class AddProductForm(forms.ModelForm):
    class Meta:
        model = AddProduct
        fields = '__all__'  # Includes all model fields