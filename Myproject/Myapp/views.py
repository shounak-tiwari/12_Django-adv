from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

# import model
from .models import  Item
# import forms 
from .forms import ItemForms


# crete add views 
def Item_create(request):
    # post
    if request.method == "POST":
        form = ItemForms(request.POST,request.FILES) # handle image upload
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForms()
    return render(request,'item_form.html',{'form':form})


# read items 
def item_list(request):
    items = Item.objects.all()
    return render(request,'read.html',{'items' : items})


# update items 
def item_update(request,id):
    item = get_object_or_404(Item , id =id)
    if request.method =="POST":
        form = ItemForms(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form= ItemForms(instance=item)
    return render(request,'item_form.html',{'form':form})

# delete items 

def item_delete(request,id):
    item = get_object_or_404(Item,id=id)

    if request.method =="POST":
        item.delete()
        return redirect("item_list")
    
    return render(request,'delete.html' ,{'item':item})