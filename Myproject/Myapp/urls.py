from django.urls import path
from .views import item_list, item_update, Item_create,item_delete

urlpatterns = [
    path('',item_list,name='item_list'),
    path('add/',Item_create,name="Item_create"),
    path('edit/<int:id>/',item_update,name='item_update'),
    path('delete/<int:id>',item_delete,name="item_delete")
]
