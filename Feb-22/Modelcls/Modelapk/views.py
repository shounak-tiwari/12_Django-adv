from django.shortcuts import render, redirect
from .forms import AddProductForm  # Import your form
from .models import AddProduct  # Import your model

def AddProductViews(request):
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)  # ✅ Correctly passing POST & FILES
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect after saving
    else:
        form = AddProductForm()  # ✅ No parameters for GET requests

    return render(request, 'Addproduct.html', {'form': form})
