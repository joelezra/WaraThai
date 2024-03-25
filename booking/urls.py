from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking_view, name='booking'),
    path('booking-success/', views.booking_success, name='booking_success'),
]