from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib import messages

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.save()
            messages.success(request, 'Your booking has been made successfully!')
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})

def booking_success(request):
    return render(request, 'booking/booking_success.html')