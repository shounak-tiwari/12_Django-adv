from django.contrib import admin
from django.urls import path,include
# import settings of django 

from django.conf import settings
from django.conf.urls.static import static

# import myapp urls.py in project urls 

from Myapp import urls

urlpatterns = [
    path('',include(urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
