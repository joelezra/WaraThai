"""
URL configuration for warathai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include 
from home import views as index_views
from menu import views as menu_views
from booking import views as booking_views
from user_profile import views as user_profile_views

from django.urls import path, include
from home.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('booking/', booking_views.booking, name='booking'),
    path('menu/', menu_views.menu, name='menu'),
    path('userprofile/', user_profile_views.user_profile, name='user-profile'),
    path('accounts/', include("allauth.urls")),
    path('admin/', admin.site.urls),
]
