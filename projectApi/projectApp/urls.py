from django.urls import path
from .views import item_list,create_item

urlpatterns = [
    path('',item_list,name="item_list"),
    path('created/',create_item,name="create_item")
]   
