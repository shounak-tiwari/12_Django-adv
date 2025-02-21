from django.contrib import admin
from django.urls import path,include
from App_name import urls

# inclue is responsible for add file path of project

urlpatterns = [
    path('',include(urls)),
    path('admin/', admin.site.urls),
]
