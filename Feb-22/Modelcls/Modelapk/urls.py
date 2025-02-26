from django.urls import path
from .views import *

urlpatterns = [
    path('',AddProductViews,name='AddProductViews')
    
]
