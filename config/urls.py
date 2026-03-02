"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import core
from core.views import index 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('', index, name='index'), # home page

    path('contact/', core.views.contact, name='contact'), # contact page

    path('admin/', admin.site.urls),
    # path('', include('core.urls')), 
    

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) ## this is to serve media files during development, it will serve media files from the MEDIA_URL and MEDIA_ROOT defined in the settings.py file    
