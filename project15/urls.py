"""project15 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app.views import *
from app2.views import *
from app3.views import *
from app4.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jinga_app2/',jinga_app2,name='jinga_app2'),
    path('apptwo/',apptwo,name='apptwo'),
    path('app3/',app3,name='app3'),
    path('app4/',app4,name='app4'),
]
