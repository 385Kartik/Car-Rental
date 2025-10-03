from django.shortcuts import render

# bookings/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from cars.models import Car
from datetime import datetime

@login_required
def create_booking_view(request, car_pk):
    car = Car.objects.get(pk=car_pk)
    if request.method == 'POST':
        pickup_date_str = request.POST.get('pickupDate')
        return_date_str = request.POST.get('returnDate')
        
        pickup_date = datetime.strptime(pickup_date_str, '%Y-%m-%d').date()
        return_date = datetime.strptime(return_date_str, '%Y-%m-%d').date()
        
        num_days = (return_date - pickup_date).days
        total_price = num_days * car.price_per_day

        Booking.objects.create(
            user=request.user,
            car=car,
            pickup_date=pickup_date,
            return_date=return_date,
            total_price=total_price,
        )
        return redirect('my_bookings')
    # This view is mainly for processing the form, which is on the car_detail page.
    return redirect('car_detail', pk=car_pk)

@login_required
def my_bookings_view(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-pickup_date')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})
