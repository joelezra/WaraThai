from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.booking_view, name='booking'),
    path('booking-success/', views.booking_success, name='booking_success'),
]