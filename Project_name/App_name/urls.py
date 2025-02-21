from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('about/',about,name='about'),
    path('load_data/',load_data,name="load_data")
]


'''
inside the path name is a use for redirect methods genrally it a name of urls 
'''