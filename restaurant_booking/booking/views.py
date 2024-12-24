from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from datetime import time, datetime

# Restaurant opening hours and open days
OPENING_HOURS = (18, 23)  # 6 PM to 11 PM
DAYS_OPEN = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def is_restaurant_open(booking_date, booking_time):
    weekday_name = booking_date.strftime('%A')
    if weekday_name not in DAYS_OPEN:
        return False
    return time(OPENING_HOURS[0], 0) <= booking_time <= time(OPENING_HOURS[1], 0)

def home(request):
    return render(request, 'booking/home.html')

def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_date = form.cleaned_data['date']
            booking_time = form.cleaned_data['time']

            # Check if the restaurant is open
            if not is_restaurant_open(booking_date, booking_time):
                return render(request, 'booking/make_booking.html', {
                    'form': form,
                    'error': 'The restaurant is closed at this time.',
                })

            # Save the booking
            form.save()
            return redirect('view_bookings')
    else:
        form = BookingForm()

    return render(request, 'booking/make_booking.html', {'form': form})

def view_bookings(request):
    bookings = Booking.objects.all().order_by('date', 'time')
    return render(request, 'booking/view_bookings.html', {'bookings': bookings})
