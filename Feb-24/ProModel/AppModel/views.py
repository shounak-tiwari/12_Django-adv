from django.shortcuts import render, redirect,get_object_or_404
from .models import AddProduct
from .forms import AddProductForm

def Showproduct(request):
    # read data from database 
    dataread = AddProduct.objects.all()
    return render(request,'Showproduct.html',{'dataread':dataread})

def Addproductviews(request):
    if request.method == "POST":
        temp = AddProductForm(request.POST)        
        if temp.is_valid():
            temp.save()
        redirect('Showproduct')
    else:
        temp = AddProductForm()
    return render(request, 'Addproduct.html', {'form': temp})